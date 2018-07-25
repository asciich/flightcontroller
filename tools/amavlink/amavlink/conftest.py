import os
import sys
import time

import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from AMavlink import AMavlink
from AMavlinkEnums import AMavlinkEnums
import docker


class SitlContainer(object):

    def __init__(self, container_command):
        self._client = docker.from_env()
        self._container = None
        self._container_command = container_command
        self.run()

    def kill(self):
        self._container.kill()
        self._container = None

    def reset(self):
        self.kill()
        self.run()

    def run(self):
        image = 'asciich/ardupilot_sitl:3.5.7'
        self._container = self._client.containers.run(image,
                                                      self._container_command,
                                                      detach=True,
                                                      auto_remove=True,
                                                      network_mode='host',
                                                      tty=True)
        self._wait_ready()

    def logs(self):
        return self._container.logs().decode()

    def _wait_ready(self):
        for i in range(1000):
            if 'APM: EKF2 IMU1 tilt alignment complete' in self.logs():
                break
            else:
                time.sleep(0.1)


@pytest.fixture(scope='session')
def arducopter_sitl():
    sitl_container = SitlContainer('sim_arducopter')
    yield sitl_container
    sitl_container.kill()


@pytest.fixture
def is_python3():
    if sys.version_info.major == 3:
        return True
    else:
        return False


@pytest.fixture
def amavlink():
    mavlink = AMavlink(port=14550)
    yield mavlink
    mavlink.close()


@pytest.fixture
def enums():
    return AMavlinkEnums()
