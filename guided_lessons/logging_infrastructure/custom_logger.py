import inspect
import logging


def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stacak()[1][3]

    # By default, log all messages