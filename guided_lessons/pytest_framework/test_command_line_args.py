import pytest


def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")


def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")


def pytest_addoption(parser):
    parser.addoption("--broswer")
    parser.addoption("--osType", help="Type of opertaing system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
