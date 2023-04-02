import logging.config
from application.mod7.task7.config_dict import config_dict

logger = logging.getLogger('Calc app')

logging.config.dictConfig(config_dict)

if __name__ == '__main__':
    while True:
        msg = input()
        logger.info(msg)
