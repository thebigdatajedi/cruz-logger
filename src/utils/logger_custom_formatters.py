import logging
from logging import Formatter, LogRecord, FileHandler, DEBUG
import json
from typing import Any


class ObjectGraphCustomFormatter(Formatter):
    def __init__(self, fmt=None, datefmt=None, logging_level_enum=None):
        self.logging_level_enum = logging_level_enum
        super().__init__(fmt, datefmt)

    def format(self, record: LogRecord):
        obj: Any = record.msg
        if record.levelno < self.logging_level_enum:  # logging level enum checked and if less than this value
            # throws exception
            raise logging.Filterer()
        json_representation_of_object_graph = json.dumps(obj.__dict__, indent=2, sort_keys=True)
        class_name = type(obj).__name__
        flattened_json_representation_of_object_graph = json_representation_of_object_graph.replace('\n', ' ').rstrip()
        cleaned_up_and_flattened_json_representation_of_object_graph = flattened_json_representation_of_object_graph.replace(
            '  ', '')
        flattened_object_graph = f'{class_name}: {cleaned_up_and_flattened_json_representation_of_object_graph}\n'
        record.msg = flattened_object_graph
        return super().format(record)

