from mocks.control4_driver import Control4Driver
from mocks.crestron_driver import CrestronDriver
from mocks.rti_driver import RTIDriver


def test_keepalive_keeps_driver_online(control4_driver, clock):
    control4_driver.connect()
    assert control4_driver.status == "Online"

    for _ in range(20):
        clock.advance(30)
        control4_driver.keepalive()

    assert control4_driver.status == "Online"


def test_keepalive_interval_is_less_than_device_idle_timeout():
    device_idle_timeout = 300
    for cls in (Control4Driver, RTIDriver, CrestronDriver):
        assert cls.keepalive_interval < device_idle_timeout, (
            f"{cls.__name__} keepalive interval must be < device idle timeout"
        )
