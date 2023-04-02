import logging


class FileLevelLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        message = self.format(record)
        level_name = record.levelname.lower()
        with open(f'logs/calc_{level_name}.log', "a+") as f:
            f.write(f"{message}\n")
