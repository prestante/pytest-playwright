import pytest

@pytest.fixture()
def prepare():
    print("\nPrepare")
    yield
    print("Postpare")
    
def test_step1():
    print("Step1")

def test_step2(prepare):
    print("Step2")