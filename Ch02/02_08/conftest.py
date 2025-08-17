import pytest
from api_client import APIClient


@pytest.fixture
def client():
    # setup
    client = APIClient('localhost')

    yield client

    # teardown
    client.close()
