# pyTest filename should starts with "test_" keyword
# Test should always be in method/function
# Test method should also starts with "test_" keyword
import pytest

@pytest.mark.smoke
@pytest.mark.xfail
def test_method1():
    print("test method 1")


def test_method2():
    print("test method 2")


# Running pytest tests from command line
# py.test -> runs all the tests recognized by pyest within the current path
# py.test -v -> for more details of test execution (verbose)
# py.test -s -> for printing console logs
# py.test <tests_path> -> to run specific tests
# Run specific test file - py.test section18-pytest/test_demo2.py
# Run specific test methods name using regular expression(-k) - py.test -k demo -v -s
# Grouping test using @pytest.mark.smoke: py.test -m smoke -v -s
# Skipping tests : @pytest.mark.skip
# Run known failure tests but avoid reporting it: @pytest.mark.xfail

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
