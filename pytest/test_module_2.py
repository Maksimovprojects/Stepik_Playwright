import pytest


@pytest.fixture(scope='function')
def pre_setup():
    print("prepare_ setup")
    return "start"

@pytest.fixture(scope='function')
def post_execution():
    print("I setup module instance for post_execution")
    yield
    print("finishing_teardown")

@pytest.mark.smoke
def test_3(pre_setup, post_execution):
    print("Test_3_started")
    assert pre_setup == "start"
    print("Test_3_finished")

@pytest.mark.skip
def test_4(pre_setup_conf):
    print("Test_4_started")
    assert 4 == 4




