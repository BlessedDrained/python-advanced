from mod4.task1 import app
import unittest


class RegistrationEndpointTest(unittest.TestCase):

    #region setup
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.form_data = dict(
            email='pochta@mail.ru',
            phone=9999999998,
            name='user',
            address='nowhere',
            index=620000,
            comment='empty')

        self.uri = '/registration'

    #endregion

    #region email
    def test_email_fail(self):
        self.form_data['email'] = 'noemail'
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_email_success(self):
        self.form_data['email'] = 'user@mail.com'
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)
    #endregion

    #region phone
    def test_phone_fail_1(self):
        self.form_data['phone'] = '150'
        response = self.app.post(self.uri, data=self.form_data)
        response_text = response.data.decode()
        self.assertEqual(200, response.status_code)

    def test_phone_fail_2(self):
        self.form_data['phone'] = 150
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_phone_success(self):
        self.form_data['phone'] = 9221543084
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    #endregion

    #region name
    def test_name_fail(self):
        self.form_data['name'] = ''
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_name_success(self):
        self.form_data['name'] = 'user'
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)
    #endregion

    #region address
    def test_address_fail(self):
        self.form_data['address'] = ''
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_address_success(self):
        self.form_data['address'] = 'address'
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)
    #endregion

    #region index
    def test_index_fail(self):
        self.form_data['index'] = ''
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_index_success(self):
        self.form_data['index'] = 620000
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    #endregion

    #region comment
    def test_comment_fail(self):
        self.form_data['comment'] = ''
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    def test_comment_success(self):
        self.form_data['comment'] = 'comment'
        response = self.app.post(self.uri, data=self.form_data)
        self.assertEqual(200, response.status_code)

    #endregion