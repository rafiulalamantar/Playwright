import pytest


@pytest.fixture
def preSetupWork(scope="session"):
    print("I set up browser instance")