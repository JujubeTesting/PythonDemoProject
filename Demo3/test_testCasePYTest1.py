import pytest
@pytest.yield_fixture()
def beforeTest():
    print("runs before everyTest")
    yield
    print("runs after every test")
def testCase4(beforeTest):
    print("pyTest 1 executed")

def testCase5(beforeTest):
    print("pyTest 2 executed")