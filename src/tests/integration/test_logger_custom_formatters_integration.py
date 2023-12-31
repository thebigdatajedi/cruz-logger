import logging
from logging import Logger
from src.utils.logger_custom_formatters import ObjectGraphCustomFormatter
from src.utils.logger_custom_handler import ObjectGraphCustomRotatingFileHandler
from src.utils.reader_for_logger_custom_formatters_integration_tests import \
    get_last_log_line_for_integration_test_assertion


# We are going to be using this configuration for building the CLI
def test_object_graph_rotating_file_handler_with_object_graph_custom_formatter():
    # Arrange - Act - Assert
    # Use the ru_all_test.sh and this is the correct relative path because the relative path is based on
    # working directory of the terminal and not the file.
    log_file_path = 'test_logs/test.log'

    # Arrange
    # Arranging the class that will be logged.
    class Truck:
        def __init__(self, name, body_color, size):
            self.id = 33
            self.name = name
            self.body_color = body_color
            self.size = size

    try:
        # Arranging the expected values for the assertions at the end of the test.
        expected_level_name = 'INFO'
        expected_body_color = 'Black'
        expected_class_name = 'Truck'
        expected_name = 'Stella'
        expected_size = 'monster'
        expected_id = 33

        # Arranging the object that will be logged.
        stella = Truck('Stella', 'Black', 'monster')
        # Arranging the logger and handler.
        logging_level: int = logging.DEBUG
        logger = Logger(__name__)
        # This handler is more for enterprise level logging.
        handler = ObjectGraphCustomRotatingFileHandler(log_file_path,
                                                       maxBytes=60000000,
                                                       backupCount=5)
        handler.setLevel(logging_level)
        handler.setFormatter(ObjectGraphCustomFormatter('%(asctime)s %(levelname)s %(msg)s',
                                                        None,
                                                        logging_level))
        logger.addHandler(handler)

        # Act
        # Acting is logging the object.
        logger.info(stella)
    except AttributeError as a:
        print(a)
        assert False
    except TypeError as t:
        print(t)
        assert False
    except Exception as e:
        print(e)
        assert False

    # Assert - getting the data from the log to assert against.
    record_last_logged = get_last_log_line_for_integration_test_assertion(log_file_path)

    # Asserting the data from the log against the expected values.
    assert expected_level_name in record_last_logged
    assert expected_body_color in record_last_logged
    assert expected_class_name in record_last_logged
    assert expected_name in record_last_logged
    assert expected_size in record_last_logged
    assert str(expected_id) in record_last_logged


def test_object_graph_rotating_file_handler_with_object_graph_custom_formatter_with_python_builtins():
    pass


def test_object_graph_rotating_file_handler_with_object_graph_custom_formatter_with_python_builtins_data_classes():
    pass


def test_object_graph_and_python_builtins_classes_with_static_vars_and_instance_vars():
    pass


def test_object_graph_and_python_builtins_classes_with_static_vars_and_instance_vars_and_instance_methods():
    pass


def test_o_g_and_python_builtins_classes_with_static_vars_and_instance_vars_and_instance_methods_and_static_methods():
    pass

# is a class method and a static method the same thing in Python?
