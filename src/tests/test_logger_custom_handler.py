from logging import Logger, DEBUG

from src.utils.config.logger_config import PreConfigObjGraphCustomFmtAndHndlLogger
from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter
from src.utils.logger_custom_handler import ObjectGraphCustomRotatingFileHandler


def test_object_graph_custom_handler_is_returned_by_logger():
    # Arrange
    test_log = 'test_logs/test.log'
    logger = PreConfigObjGraphCustomFmtAndHndlLogger.create()
    logger.set_main_log(test_log)
    handler = logger.get_handler()

    # Check if the formatter is being used by the handler
    # Assert
    handler_in_logger = logger.get_handler()
    handler_outside_of_logger = handler
    if handler_in_logger is handler_outside_of_logger:
        assert True
    else:
        assert False
