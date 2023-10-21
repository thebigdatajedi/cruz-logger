import json
import logging
from logging.handlers import RotatingFileHandler
from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter


class ObjectGraphCustomRotatingFileHandler(RotatingFileHandler):
    def __init__(self, filename=None, mode='a', maxBytes=1000000, backupCount=10):
        super().__init__(filename, mode, maxBytes, backupCount)

    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(msg)
            self.flush()
        except ValueError as v:
            self.handleError(record)
        except TypeError as t:
            self.handleError(record)
