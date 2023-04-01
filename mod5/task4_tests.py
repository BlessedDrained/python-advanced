import unittest
from task4 import Redirect


class Task4Test(unittest.TestCase):
    def test_stdout(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout:
            content = stdout.read()
            self.assertTrue('Hello stdout.txt' in content)

    def test_stderr(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stderr.txt') as stderr:
            content = stderr.read()
            self.assertTrue("Exception: Hello stderr.txt" in content)

    def test_none_stderr(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stdout=stdout_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stderr.txt') as stderr:
            content = stderr.read()
            self.assertTrue("Exception: Hello stderr.txt" not in content)

    def test_none_stdout(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout:
            content = stdout.read()
            self.assertTrue('Hello stdout.txt' not in content)

    def test_none_args(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect():
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout, open('stderr.txt') as stderr:
            out_content = stdout.read()
            err_content = stderr.read()
            self.assertTrue('Hello stdout.txt' not in out_content and "Exception: Hello stderr.txt" not in err_content)
