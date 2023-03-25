import os
import signal
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def release_app_with_port(port: int):
    cmd = f"lsof -i :{port}".split()
    run_result = subprocess.run(cmd, capture_output=True)
    processes_list = run_result.stdout.decode()
    for row in processes_list:
        pid = int(row.split()[1])
        os.kill(pid, signal.SIGKILL)
    app.run()


if __name__ == '__main__':
    release_app_with_port(5000)