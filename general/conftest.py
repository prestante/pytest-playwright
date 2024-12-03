import pytest

@pytest.fixture(autouse=True, scope='package')
def log_test():
    print("\nTest is starting")
    yield
    print("\nTest is ending")