from logging.handlers import TimedRotatingFileHandler

from application.mod7.task3.FileLevelLogHandler import FileLevelLogHandler
from application.mod7.task5.ModuleNameFilter import ModuleNameFilter
from application.mod7.task7.LogFilter import LogFilter

config_dict = {
    'version': 1,
    'filters': {
        'LogFilter': {
            '()': LogFilter
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            '()': FileLevelLogHandler,
            'level': 'INFO',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'Calc app': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        },
        'Calc utils': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }
}

