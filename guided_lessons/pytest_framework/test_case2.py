import pytest


@pytest.fixture()
def setUp():
    print("Running demo2 setup")
    yield
    print("Running demo2 tear down")


def test_methodA(setUp):
    print("Running demo2 method A")


def test_methodB(setUp):
    print("Running demo2 method B")
