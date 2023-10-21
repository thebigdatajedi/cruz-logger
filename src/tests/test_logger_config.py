from logging import Logger, DEBUG
from src.utils.config.logger_config import PreConfigObjGraphCustomFmtAndHndlLogger
from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter
from src.utils.logger_custom_handler import ObjectGraphCustomRotatingFileHandler


def test_create_pre_config_obj_graph_custom_fmt_and_hndl_logger_test_is_a_pr_config_obj_graph_cust_fmt_hndl_logger():
    logger = PreConfigObjGraphCustomFmtAndHndlLogger.create()
    logger.set_main_log('test_logs/test.log')
    is_a_logger = isinstance(logger, PreConfigObjGraphCustomFmtAndHndlLogger)
    assert is_a_logger


def test_create_pre_config_obj_graph_custom_fmt_and_hndl_logger_is_a_logger():
    logger = PreConfigObjGraphCustomFmtAndHndlLogger.create()
    logger.set_main_log('test_logs/test.log')
    is_a_logger = isinstance(logger, Logger)
    assert is_a_logger


def test_object_graph_custom_formatter_is_returned_by_object_graph_custom_rotating_file_handler():
    # Arrange
    # Create a logger
    logger = PreConfigObjGraphCustomFmtAndHndlLogger.create()
    logger.set_main_log('test_logs/test.log')

    # Act
    formatter_in_pre_config_logger = logger.get_formatter()

    # Assert
    assert isinstance(formatter_in_pre_config_logger, ObjectGraphCustomFormatter)


def test_object_graph_custom_handler_is_returned_by_pre_confi_obj_graph_custom_fmt_and_hndl_logger():
    # Arrange
    # Create a logger
    logger = PreConfigObjGraphCustomFmtAndHndlLogger.create()

    # Act
    handler_in_pre_config_logger = logger.get_handler()

    # Assert
    assert isinstance(handler_in_pre_config_logger, ObjectGraphCustomRotatingFileHandler)
