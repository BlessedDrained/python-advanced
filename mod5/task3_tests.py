from task3 import BlockErrors
import unittest


class Task3Test(unittest.TestCase):
    def test_ignore_error(self):
        err_types = {ZeroDivisionError}
        try:
            with BlockErrors(err_types):
                a = 1 / 0
        except:
            self.fail()

    def test_error_raises(self):
        err_types = {ZeroDivisionError}
        try:
            with BlockErrors(err_types):
                a = 1 / '0'
            self.fail()
        except TypeError:
            pass

    def test_internal_error_is_ignored_in_external(self):
        outer_err_types = {TypeError}
        try:
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                try:
                    with BlockErrors(inner_err_types):
                        a = 1 / '0'
                    self.fail()
                except TypeError:
                    pass
        except TypeError:
            self.fail()

    def test_derived_errors_are_ignored(self):
        err_types = {Exception}
        try:
            with BlockErrors(err_types):
                a = 1 / '0'
        except:
            self.fail()
