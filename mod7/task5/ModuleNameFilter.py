import logging


class ModuleNameFilter(logging.Filter):
    def filter(self, record):
        return record.name == "utils"
