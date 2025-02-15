# pyTest filename should starts with "test_" keyword
# Test should always be in method/function - Test method
# should also starts with "test_" keyword
import pytest


def test_method3():
    print("test method 3")


def test_method4():
    msg = "Hello"
    assert msg == "hi", "Test failed because condition string do not match"


# Running pytest tests from command line
# py.test -> runs all the tests recognized by pyest within the current path
# py.test -v -> for more details of test execution (verbose)
# py.test -s -> for printing console logs
# py.test <tests_path> -> to run specific tests
# Run specific test file - py.test section18-pytest/test_demo2.py
# Run specific test methods name using regular expression(-k) - py.test -k demo -v -s


def test_fixture_demo(setup):
    print("I will execute steps in fixture demo method")


