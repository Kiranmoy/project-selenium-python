import pytest
from base import base


@pytest.mark.usefixtures("data_load")
class TestFixtureDataDemo(base):

    def test_editProfile(self, data_load): # pass data fixture name as argument
        log = self.get_logger()
        log.info(data_load)
        log.info(data_load[0])
        log.info(data_load[1])
        log.info(data_load[2])