from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
import subprocess

app = Flask(__name__)


class Form(FlaskForm):
    class Meta:
        csrf = False

    input = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired()])


@app.route('/wtf', methods=['POST'])
def func():
    form = Form()
    split_cmd = 'prlimit --nproc=1:1 python -c'.split()
    subprocess.Popen(split_cmd, shell=True)
    if form.validate_on_submit():
        cmd = f'python -c "{form.input.data}"'
        time = form.timeout.data
        if time > 30:
            return 'Время вышло'
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).stdout.read()
        decoded_output = output.decode()
        return decoded_output


if __name__ == "__main__":
    app.run()
