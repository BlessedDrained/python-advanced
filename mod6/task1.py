from flask import Flask
from wtforms import StringField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from application.mod4.task2 import number_length, NumberLength
import logging


class RegistrationForm(FlaskForm):
    class Meta:
        csrf = False

    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10, 10, 'Incorrect number length')])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[InputRequired()])


logging.basicConfig(
    filename='stderr.txt',
    filemode='a',
    format='[%(asctime)s] Source: %(name)s | Level: %(levelname)s | Message: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger('AuthLogger')
app = Flask(__name__)


@app.route('/registration', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        logger.info(f"Successfully registered user {email} with phone +7{phone}")
        return f"Successfully registered user {email} with phone +7{phone}"
    logger.error(f"{form.errors}")
    return f"{form.errors}", 400


if __name__ == '__main__':
    app.run(debug=True)
