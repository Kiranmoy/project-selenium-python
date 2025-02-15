import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureDemo():

    def test_fixturedemo0(self):
        print("fixture_demo_0")

    def test_fixturedemo1(self):
        print("fixture_demo_1")

    def test_fixturedemo2(self):
        print("fixture_demo_2")

    def test_fixturedemo3(self):
        print("fixture_demo_3")