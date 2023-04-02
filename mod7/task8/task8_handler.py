import logging.config
from application.mod7.task8.task8_config import config_dict

logging.config.dictConfig(config_dict)

logger = logging.getLogger('test')
logger.info('Test message')
