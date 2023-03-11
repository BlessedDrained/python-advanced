from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:path>')
def max_number(path):
    try:
        values = list(map(int, path.split("/")))
    except:
        return "Values contain non-numeric value"

    return f"Максимальное переданное число <i>{max(values)}</i>"


if __name__ == '__main__':
    app.run()
