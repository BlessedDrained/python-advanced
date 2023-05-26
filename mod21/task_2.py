from mod21.task_1 import Book, Author, Student, ReceivingBook
import datetime
from flask import Flask, jsonify
from sqlalchemy import create_engine, func, extract, desc
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

app = Flask(__name__)

engine = create_engine('sqlite:///sqlite_python.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

if __name__ == '__main__':
    app.run(port=5001)


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/books/remaining/<int:author_id>', methods=['GET'])
def get_remaining_books(author_id):
    author = session\
        .query(Author)\
        .filter(Author.id == author_id)\
        .first()

    if author is None:
        return f"Author with id={author_id} is not found", 400

    count = 0
    for book in author.book:
        count += book.count

    return jsonify({f'Author with id={author_id} has books left': count})


@app.route('/books/unread/<int:student_id>', methods=['GET'])
def get_unread_books(student_id):
    student = session.query(Student).get(student_id)
    if not student:
        return f"Student with с id={student_id} has not been found", 400

    student_book_ids = [receiving_book.book_id for receiving_book in student.receiving_books]

    author_book_ids = session\
        .query(Book.id)\
        .filter(Book.author_id.in_([book.author_id for book in student.receiving_books]))\
        .subquery()

    unread_books = session\
        .query(Book)\
        .filter(Book.id.in_(author_book_ids))\
        .filter(~Book.id.in_(student_book_ids))\
        .all()

    return jsonify({'Read book list': [book.name for book in unread_books]})


@app.route('/books/average', methods=['GET'])
def get_average_books():
    current_month = datetime.datetime.now().month


    books_count = session.query(func.avg(func.count(ReceivingBook.book_id))) \
        .filter(extract('date_of_issue', ReceivingBook.received_date) == current_month).scalar()

    return f"Average book borrowed by students for this month count is {books_count}"


@app.route('/books/popular', methods=['GET'])
def get_popular_book():
    popular_book = session.query(ReceivingBook.book_id, func.count(ReceivingBook.book_id)).\
        join(Student).\
        filter(Student.average_score > 4.0).\
        group_by(ReceivingBook.book_id).\
        order_by(func.count(ReceivingBook.book_id).desc()).\
        first()

    if popular_book:
        book = session.query(Book).get(popular_book[0])
        return f"The most popular book with rating above 4.0 is {book.name}"
    else:
        return "No popular books there"


@app.route('/students/top-10-readers', methods=['GET'])
def get_top_readers():
    current_year = date.today().year
    top_readers = session.query(Student).\
        join(ReceivingBook).\
        filter(func.extract('year', ReceivingBook.received_date) == current_year).\
        group_by(Student).\
        order_by(desc(func.count(ReceivingBook.id))).\
        limit(10).\
        all()

    top_readers_data = []
    for reader in top_readers:
        reader_data = {
            'id': reader.id,
            'name': reader.name,
            'books_borrowed': len(reader.receiving_books)
        }
        top_readers_data.append(reader_data)

    return jsonify({'top_readers': top_readers_data})