import pytest

@pytest.fixture(scope="session")
def userCredentials(request):
    return request.param