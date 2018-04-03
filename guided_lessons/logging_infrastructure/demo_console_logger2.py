"""
Logger Demo
"""
import logging
import logging.config


class LoggerDemoConf():

    def testLog(self):
        # create logger

        # logging messages
        logger.debug('debug message')
        logger.info('ingo message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')


ldc = LoggerDemoConf()
ldc.testLog()
