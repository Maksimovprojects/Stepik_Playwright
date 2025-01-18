import pytest

@pytest.fixture(scope='session')
def pre_setup_conf():
    print("I setup browser instance from conftest.py")