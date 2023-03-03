import os.path

from flask import Flask
from random import choice
from datetime import datetime
from datetime import timedelta
from re import compile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']


def get_book_words():
    with open(BOOK_FILE) as book:
        words = [word for line in book for word in compile("[a-zA-Z']+").findall(line)]
    return words


words = get_book_words()

counter = 0


@app.route('/hello_world')
def hello_world():  # put application's code here
    return 'Привет, мир!'


@app.route('/cars')
def get_cars():
    return ', '.join(cars)


@app.route('/cats')
def get_cats():
    return choice(cats)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    return choice(words)


@app.route('/counter')
def get_counter_value():
    global counter
    counter += 1
    return str(counter)


if __name__ == '__main__':
    app.debug = True
    app.run()
