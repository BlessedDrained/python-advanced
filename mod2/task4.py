from datetime import datetime
from flask import Flask

app = Flask(__name__)

weekdays_tuple = (
    "понедельника",
    "вторника",
    "среды",
    "четверга",
    "пятницы",
    "cубботы",
    "воскресенья"
)


def get_regard():
    day_number = datetime.today().weekday()
    ending = "его" if day_number in (0, 1, 3, 6) else "ей"
    return f"Хорош{ending} {weekdays_tuple[day_number]}"


@app.route('/hello-world/<string:name>')
def hello_world(name):
    return f"Привет, {name}. {get_regard()}!"


if __name__ == '__main__':
    app.run()
