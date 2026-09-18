import pytest

from mocks.clock import MockClock
from mocks.control4_driver import Control4Driver
from mocks.crestron_driver import CrestronDriver
from mocks.mock_device import MockDevice
from mocks.rti_driver import RTIDriver


@pytest.fixture
def clock():
    return MockClock()


@pytest.fixture
def online_device(clock):
    return MockDevice(reachable=True, idle_timeout=300, clock=clock)


@pytest.fixture
def offline_device(clock):
    return MockDevice(reachable=False, clock=clock)


@pytest.fixture
def control4_driver(online_device):
    return Control4Driver(online_device)


@pytest.fixture
def rti_driver(online_device):
    return RTIDriver(online_device)


@pytest.fixture
def crestron_driver(online_device):
    return CrestronDriver(online_device)
