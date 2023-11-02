from logging import Logger, DEBUG
from typing import TypeVar

from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter
from src.utils.logger_custom_handler import ObjectGraphCustomRotatingFileHandler

Self = TypeVar('Self', bound='PreConfigObjGraphCustomFmtAndHndlLogger')


class PreConfigObjGraphCustomFmtAndHndlLogger(Logger):
    def __init__(self, name: str = __name__):
        self.log = "../../logs/main.log"
        self.logging_level_enum = DEBUG
        super().__init__(name)
        self.handler = ObjectGraphCustomRotatingFileHandler(self.log,
                                                            maxBytes=60000000,
                                                            backupCount=7)
        self.formatter = ObjectGraphCustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                                    None,
                                                    self.logging_level_enum)
        self.handler.setFormatter(self.formatter)
        self.logger = Logger(name)
        self.logger.setLevel(self.logging_level_enum)
        super().setLevel(self.logging_level_enum)
        self.logger.addHandler(self.handler)

    @staticmethod
    def create() -> Self:
        pre_configured_logger_with_rotating_file_handler: Self = PreConfigObjGraphCustomFmtAndHndlLogger()
        return pre_configured_logger_with_rotating_file_handler

    def get_formatter(self) -> ObjectGraphCustomFormatter:
        return self.formatter

    def get_handler(self) -> ObjectGraphCustomRotatingFileHandler:
        return self.handler

    def set_main_log(self, main_log: str):
        self.log = main_log
