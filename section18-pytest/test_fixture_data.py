import pytest
from base import base


@pytest.mark.usefixtures("data_load")
class TestFixtureDataDemo(base):

    def test_editProfile(self, data_load):
        log = self.get_logger()
        log.info(data_load)
        log.info(data_load[0])
        log.info(data_load[1])
        log.info(data_load[2])