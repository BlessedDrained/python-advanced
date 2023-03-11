import unittest
from person import Person


class PersonTest(unittest.TestCase):
    def test_init(self):
        person = Person('John', 2001, 'Nowhere')
        expected = ['John', 2001, 'Nowhere']
        self.assertEqual(expected, [person.name, person.yob, person.address])

    def test_get_age(self):
        person = Person('John', 2001, 'Nowhere')
        expected = 22
        self.assertEqual(expected, person.get_age())

    def test_get_name(self):
        person = Person('John', 2001, 'Nowhere')
        expected = 'John'
        self.assertEqual(expected, person.get_name())

    def test_set_name(self):
        person = Person('John', 2001, 'Nowhere')
        person.set_name('Dave')
        expected = 'Dave'
        self.assertEqual(expected, person.get_name())

    def test_get_address(self):
        person = Person('John', 2001, 'Nowhere')
        expected = 'Nowhere'
        self.assertEqual(expected, person.get_address())

    def test_set_address(self):
        person = Person('John', 2001, 'Nowhere')
        person.set_address('Here')
        expected = 'Here'
        self.assertEqual(expected, person.get_address())

    def test_is_homeless(self):
        person = Person('John', 2001, 'Nowhere')
        self.assertFalse(person.is_homeless())
