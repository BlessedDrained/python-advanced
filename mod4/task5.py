from flask import Flask
from flask import request
import shlex
import subprocess

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def get_ps():
    args_raw = request.args.getlist('arg')
    args = "".join([shlex.quote(x) for x in args_raw])
    command = f"ps {args}".split()
    run_result = subprocess.run(command, capture_output=True)

    if run_result.returncode != 0:
        return "Internal server error", 500

    cmd_output = run_result.stdout.decode()
    return f"<pre>Your result: {cmd_output}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
