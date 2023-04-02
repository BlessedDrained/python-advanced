import logging
import string


class LogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        for char in record.msg:
            if char in string.printable:
                return False
        return True
