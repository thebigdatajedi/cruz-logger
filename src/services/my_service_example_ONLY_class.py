import logging


class MyServiceWithMethodsThatExplainScopeOfTheseTypeOfClassesClass:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    # Methods that accept the keyword self and operate of self are instance methods.
    def do_something_that_operates_only_on_the_business(self):
        self.logger.info('Doing something')

    def these_methods_can_be_static_or_instance_methods(self):
        self.logger.info('this is an instance method')

    # Service classes usually have both kinds of methods depending on the class need and how the code is organized.
    # I've not used the @staticmethod decorator before but look legit, all I've done in the past is not pass itself.
    @staticmethod
    def my_static_method_that_does_more_domain_specific():
        print('This is a static method')
