import logging
import custom_logger as cl


class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('ingo message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        self.log.debug('debug message')
        self.log.info('ingo message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method3(self):
        self.log.debug('debug message')
        self.log.info('ingo message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')


ld = LoggingDemo2()
ld.method1()
ld.method2()
ld.method3()
