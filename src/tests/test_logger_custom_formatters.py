from logging import Logger, DEBUG
from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter
from src.utils.logger_custom_handler import ObjectGraphCustomRotatingFileHandler


def test_object_graph_custom_formatter_is_returned_by_object_graph_custom_rotating_file_handler():
    # Arrange
    log = 'test_logs/test.log'
    logger = Logger(__name__)
    logger.setLevel(DEBUG)
    handler = ObjectGraphCustomRotatingFileHandler(log,  maxBytes=6000000, backupCount=7)

    # Act
    formatter = ObjectGraphCustomFormatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Check if the formatter is being used by the handler
    # Assert
    formatter_in_handler = handler.formatter
    formatter_outside_of_handler = formatter
    if formatter_in_handler is formatter_outside_of_handler:
        assert True
    else:
        assert False
