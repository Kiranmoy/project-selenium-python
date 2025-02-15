import pytest


# fixture are used for setup & teardown steps for test cases.
# fixture defined in conftest.py file will by default available for all the pytest test files.

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield  # post requisite steps
    print("I will be executing last")


@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["Kiranmoy", "Paul", "mrpaul@gmail.com"]


@pytest.fixture(params=[("chrome", "Kiran"), "firefox", "ie"])
def crossBrowser(request):
    return request.param
