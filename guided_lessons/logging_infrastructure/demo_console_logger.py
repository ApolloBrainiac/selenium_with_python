"""
Logger Demo
"""
import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger

        # create console handler and set level to info

        # create formatter

        # add formatter to console handler -> ch

        # add console handler to logger


        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')

ldc = LoggerDemoConsole()
ldc.testLog()