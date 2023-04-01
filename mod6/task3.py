import json
import logging
import getpass
import hashlib
from task2 import is_strong_password


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = msg.replace('"', "'")
        msg = json.dumps(msg)
        msg = msg.replace('"', "")
        return msg, kwargs


logging.basicConfig(
    filename='stderr.txt',
    filemode='a',
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

words = None
logger = JsonAdapter(logging.getLogger('AuthLogger'), extra=None)


def input_and_check_password():
    password = getpass.getpass('Enter the password: ')
    if not password:
        logger.warning('Input password is empty')
        return False
    if not is_strong_password(password, words):
        logger.info('Password contains english word(s). Try another one')
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as exception:
        logger.exception('There is incorrect symbol in password: ', exc_info=exception)
    return False


if __name__ == "__main__":
    with open('words.txt', 'r') as f:
        words = set(sorted(x for x in f.read().splitlines() if len(x) > 4))
    logging.basicConfig(
        filename='stderr.txt',
        filemode='a',
        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )
    logger = logging.getLogger('AuthLogger')

    attempts_count = 3
    while attempts_count > 0:
        logger.info(f'Attempts left: {attempts_count}')
        if input_and_check_password():
            logger.info('Successful auth')
            exit(0)
        logger.error('Incorrect password')
        attempts_count -= 1

    logger.error('No attempts left')
    exit(1)
