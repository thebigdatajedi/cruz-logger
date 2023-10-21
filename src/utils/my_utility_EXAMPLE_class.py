import logging


# This is sample code only useful for demo of Utility Class

class MyUtilityWithMethodsThatExplainScopeOfTheseTypeOfClassesClass:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def do_more_generic_task_that_are_not_business_domain_tasks(self):
        self.logger.info('Doing something')

    # I've not used the @staticmethod decorator before but look legit, all I've done in the past is not pass it self.
    @staticmethod
    def my_static_method():
        print('This is a static method')
