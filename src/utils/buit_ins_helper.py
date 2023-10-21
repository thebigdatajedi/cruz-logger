import logging
from types import NoneType
from typing import Any


class BuiltInsHelper:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    @staticmethod
    def is_built_in(my_obj: Any) -> bool:
        """

        :rtype: object
        """
        result_of_built_in_bool_check: bool = False

        if isinstance(my_obj, int):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, float):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, str):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, bool):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, list):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, tuple):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, set):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, dict):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        elif isinstance(my_obj, NoneType):
            result_of_built_in_bool_check = True
            return result_of_built_in_bool_check
        else:
            return result_of_built_in_bool_check
