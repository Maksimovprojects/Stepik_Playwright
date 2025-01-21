
import pytest
import json


@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param