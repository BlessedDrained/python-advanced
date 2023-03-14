from flask import Flask

app = Flask(__name__)


@app.route('/uptime')
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime = float(f.readline().split()[0])
    return f'Current uptime is {uptime} seconds'


if __name__ == '__main__':
    app.run(debug=True)
