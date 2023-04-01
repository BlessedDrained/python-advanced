import getpass
import hashlib
import logging


def input_and_check_password():
    password = getpass.getpass()
    if not password:
        logger.warning('Input password is empty')
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError:
        pass
    return False


if __name__ == "__main__":
    logging.basicConfig(
        filename='stderr.txt',
        filemode='a',
        format='[%(asctime)s] Source: %(name)s | Level: %(levelname)s | Message: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )
    logger = logging.getLogger('AuthLogger')

    attempts_count = 3
    logger.info('Auth attempt')
    while attempts_count > 0:
        logger.info(f'Attempts left: {attempts_count}')
        if input_and_check_password():
            logger.info('Successful auth')
            exit(0)
        logger.error('Incorrect password')
        attempts_count -= 1

    logger.error('No attempts left')
    exit(1)
