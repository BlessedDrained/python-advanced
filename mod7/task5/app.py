import logging.config
from application.mod7.task3 import utils
from application.mod7.task5.config_dict import config_dict

logger = logging.getLogger('Calc app')

logging.config.dictConfig(config_dict)

if __name__ == '__main__':
    while True:
        expr = input('Input an expression: ')
        val1 = ""
        operator = ""
        val2 = ""
        for char in expr:
            if char.isdigit():
                if operator == '':
                    val1 += char
                else:
                    val2 += char
            elif char in '+-*/':
                if operator:
                    logger.error('Only one operator is possible in expression')
                    continue
                operator = char
            elif char not in ' ':
                logger.error('Input symbol is not an operator or a digit')
        if operator and val1 and val2:
            answer = utils.calculate(int(val1), int(val2), operator)
            logger.info(f'Answer is: {val1} {operator} {val2} = {answer}')
        else:
            logger.error('An error occured')
            raise ArithmeticError
