from datetime import datetime
from flask import Flask

app = Flask(__name__)

money_data = dict(dict())


@app.route('/add/<string:date>/<int:money_amount>')
def add_month_money(date, money_amount):
    try:
        date = datetime.strptime(date, "%Y%m%d")
    except:
        return "Incorrect date format"
    money_data.setdefault(date.year, {}).setdefault(date.month, 0)
    money_data[date.year][date.month] += money_amount
    return "Success"


@app.route('/calculate/<int:year>')
def get_year_money_amount(year):
    if year not in money_data.keys():
        return f"There is no data for year: {year}"
    amount = sum([x for x in money_data[year].values()])
    return str(amount)


@app.route('/calculate/<int:year>/<int:month>')
def get_year_month_money_amount(year, month):
    if year not in money_data.keys():
        return f"There is no data for year: {year}"
    if month not in money_data[year].keys():
        return f"There is no data for month: {month}"
    amount = money_data[year][month]
    return str(amount)


if __name__ == '__main__':
    app.run(debug=True)
