from flask import Flask, request
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, Date, create_engine
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
app = Flask(__name__)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_students_in_dorm(cls):
        students = session \
            .query(Student) \
            .filter(Student.scholarship) \
            .all()
        return [x.to_json() for x in students]

    @classmethod
    def get_students_above_average(cls, score):
        students = session \
            .query(Student) \
            .filter(Student.average_score > score) \
            .all()
        return [x.to_json() for x in students]


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @hybrid_property
    def get_date_with_book(self):
        if self.date_of_return is not None:
            days_count = (self.date_of_return - self.date_of_issue).days
        else:
            days_count = (datetime.datetime.now() - self.date_of_issue).days
        return days_count


@app.route('/find', methods=['GET'])
def find_book():
    query = request.args.get("name_contains")
    books = session \
        .query(Book) \
        .filter(Book.name.like("%" + query + "%")) \
        .all()
    return [x.to_json() for x in books]


@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    return [x.to_json() for x in books]


@app.route('/debtors', methods=['GET'])
def get_debtors():
    debtors = session \
        .query(ReceivingBook) \
        .filter(ReceivingBook.date_of_return is None) \
        .all()
    return [x.to_json() for x in debtors]


@app.route('/books/issue', methods=['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    issue = ReceivingBook(book_id=book_id, student_id=student_id, date_of_issue=datetime.now())
    session.add(issue)
    session.commit()
    return f'Book with id={book_id} has been issued to student with id={student_id}'


@app.route('/books/pass', methods=['POST'])
def return_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        book = session \
            .query(ReceivingBook) \
            .filter(ReceivingBook.book_id == book_id and ReceivingBook.student_id == student_id) \
            .one()
        book.date_of_issue = datetime.now()
        session.commit()
        return f'Book with id={book_id} has been passed by student with id={student_id}'
    except MultipleResultsFound:
        return 'There are multiple records with such combination of student_id and book_id'
    except NoResultFound:
        return f'No book found'


@app.before_request
def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    engine = create_engine('sqlite:///hw.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    app.run()
