import logging.config


logger = logging.getLogger('Calc utils')

def _sum(x, y):
    logger.info('Sum will be provided')
    return x + y


def _subtract(x, y):
    logger.info('Subtract will be provided')
    return x - y


def _multiply(x, y):
    logger.info('Multiply will be provided')
    return x * y


def _divide(x, y):
    if y != 0:
        logger.info('Divide will be provided')
        return x / y
    logger.error('Zero division')
    raise ZeroDivisionError


def calculate(val1, val2, operator):
    if operator == '+':
        return _sum(val1, val2)
    if operator == '-':
        return _subtract(val1, val2)
    if operator == '*':
        return _multiply(val1, val2)
    return _divide(val1, val2)
