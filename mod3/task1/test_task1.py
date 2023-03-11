from application.mod2.task4 import app
from freezegun import freeze_time
import unittest
import datetime


class TestGoodDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def check_weekday_correctness(self, day_str):
        days_strs = [
            'понедельника',
            'вторника',
            'среды',
            'четверга',
            'пятницы',
            'субботы',
            'воскресенья'
        ]
        return day_str == days_strs[datetime.datetime.weekday(datetime.datetime.now())]

    def get_weekday_from_response(self):
        response = self.app.get('/hello-world/John')
        response_text = response.data.decode()
        response_text_splitted = ''.join(x for x in response_text if x.isalpha() or x == ' ').split()
        return response_text_splitted[-1]

    @freeze_time(datetime.datetime(year=2023, month=3, day=7))
    def test_common_name_case(self):
        weekday = self.get_weekday_from_response()
        self.assertTrue(self.check_weekday_correctness(weekday))

    @freeze_time(datetime.datetime(year=2023, month=3, day=7))
    def test_greeting_in_name(self):
        weekday = self.get_weekday_from_response()
        self.assertTrue(self.check_weekday_correctness(weekday))
