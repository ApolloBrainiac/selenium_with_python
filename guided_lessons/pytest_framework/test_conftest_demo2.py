import pytest


@pytest.fixture()
def setUp():
    print("Running conftest demo2 method setUp")
    yield
    print("Running conftest demo2 method tearDown")


def test_demo1_methodA(setUp):
    print("Running conftest demo2 method A")


def test_demo2_methodB(setUp):
    print("Running conftest demo2 method B")