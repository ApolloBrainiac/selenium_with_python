"""
HOw to use test class to wrap methods under one class
Learn about autouse keywords in fixtures
Asser the result to create a real teset scenario
"""


class SomeClassToTest():

    def __init__(self, value):
        self.value = value

    def sumNumbers(self, a, b):
        return a + b + self.value
