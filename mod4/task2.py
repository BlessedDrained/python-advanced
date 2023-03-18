from dataclasses import Field
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if min < 0 or max < 0:
            raise ValueError("One of thresholds is negative value")
        if max < min:
            raise ValueError("Max threshold is less than min")
        length = len(str(field.data))
        if length < min or length > max:
            raise ValidationError("" if not message else message)

    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if self.min < 0 or self.max < 0:
            raise ValueError("One of thresholds is negative value")
        if self.max < self.min:
            raise ValueError("Max threshold is less than min")
        length = len(str(field.data))
        if length < self.min or length > self.max:
            raise ValidationError("" if not self.message else self.message)
