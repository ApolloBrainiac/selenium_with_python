import pytest


@pytest.fixture()
def setUp():
    print("Running conftest demo method setUp")
    yield
    print("Running conftest demo method tearDown")
