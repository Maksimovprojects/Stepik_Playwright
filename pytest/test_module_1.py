import pytest

@pytest.fixture(scope='module')
def pre_setup():
    print("prepare")

def test_initial_check(pre_setup):
    print("Test_1_started")
    assert 1 == 1

def test__check_validation(pre_setup):
    print("Test_2_started")
    assert 2 == 2




