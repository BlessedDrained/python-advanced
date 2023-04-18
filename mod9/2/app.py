from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/ny_days')
def get_before_new_year_days():
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    delta = new_year - today
    return f"Until NY: {delta.days}"


if __name__ == '__main__':
    app.run()
