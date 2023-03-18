from flask import Flask
from wtforms import StringField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, NumberRange


class RegistrationForm(FlaskForm):
    class Meta:
        csrf = False
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    Index = IntegerField(validators=[InputRequired()])
    Comment = StringField(validators=[InputRequired()])


app = Flask(__name__)


@app.route('/registration', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f"Successfully registered user {email} with phone +7{phone}"
    return f"{form.errors}", 400


if __name__ == '__main__':
    app.run(debug=True)
