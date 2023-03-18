from flask import Flask
from flask import request
import shlex
import subprocess

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def get_ps():
    args_raw = request.args.getlist('arg')
    args = shlex.quote("".join(args_raw))
    command = f"ps {args}".split()
    run_result = subprocess.run(command, capture_output=True)
    cmd_output = run_result.stdout
    return f"<pre>Your result: {cmd_output}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
