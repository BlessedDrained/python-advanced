from application.mod2.task7 import app
import unittest


class DecoderTest(unittest.TestCase):
    # region Setup
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # endregion

    #region TearDown
    def tearDown(self):
        self.app.get('/clear-money-data')
    #endregion

    # region AddTests
    # Проверка работы при некорректной дате
    def test_add_incorrect_date(self):
        urn = '/add/20323044/150'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertEqual('Incorrect date format', response_text)

    # Проверка работы при некорректном количестве денег
    def test_add_negative_money_amount(self):
        urn = '/add/20230730/-555150'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertTrue('404' in response_text)

    def test_add_empty_money_amount(self):
        urn = '/add/20230730/'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertTrue('404' in response_text)

    # Проверка работы при корректных входных данных
    def test_add_correct_data(self):
        urn = 'add/20200101/150'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertEqual('Success', response_text)

    # endregion

    # region CalculateYearTests
    def test_calculate_year_correct_data_1_add(self):
        add_urn = '/add/20210101/150'
        self.app.get(add_urn)
        urn = '/calculate/2021'
        response = self.app.get(urn)
        response_text = int(response.data.decode())
        self.assertEqual(150, response_text)

    # Проверка работы при несуществующем годе
    def test_calculate_year_incorrect_year(self):
        urn = '/calculate/2021'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertEqual('There is no data for year: 2021', response_text)

    # Проверка работы при корректных входных данных

    def test_calculate_year_correct_data_2_add(self):
        add_urn1 = '/add/20210629/500000'
        add_urn2 = '/add/20210630/150000'
        self.app.get(add_urn1)
        self.app.get(add_urn2)
        urn = '/calculate/2021'
        response = self.app.get(urn)
        response_text = int(response.data.decode())
        self.assertEqual(650000, response_text)

    # endregion

    # region CalculateYearMonthTests
    # Проверка работы при несуществующем годе
    def test_calculate_year_month_incorrect_year(self):
        add_urn = '/add/20220101/123000'
        self.app.get(add_urn)
        urn = '/calculate/2032/01'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertEqual('There is no data for year: 2032', response_text)

    # Проверка работы при несуществующем месяце
    def test_calculate_year_month_incorrect_month(self):
        add_urn = '/add/20220201/123000'
        self.app.get(add_urn)
        urn = '/calculate/2022/03'
        response = self.app.get(urn)
        response_text = response.data.decode()
        self.assertEqual('There is no data for month: 3', response_text)

    # Проверка работы при корректных данных
    def test_calculate_year_month_correct_data(self):
        add_urn = '/add/20220301/123000'
        self.app.get(add_urn)
        urn = '/calculate/2022/03'
        response = self.app.get(urn)
        response_text = int(response.data.decode())
        self.assertEqual(123000, response_text)
    # endregion
