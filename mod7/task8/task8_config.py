from logging.handlers import HTTPHandler

config_dict = {
    'version': 1,
    'handlers': {
        'http': {
            '()': HTTPHandler,
            'host': 'localhost:5000',
            'url': '/logs',
            'method': 'POST',
            'secure': False
        }
    },
    'loggers': {
        'test': {
            'handlers': ['http'],
            'level': 'INFO',
        }
    }
}
