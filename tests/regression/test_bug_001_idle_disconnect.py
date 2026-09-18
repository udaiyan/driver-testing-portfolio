"""Regression tests for BUG-001 — RTI driver drops connection after idle.

Bug: keepalive interval (60s) combined with the driver only sending keepalives
on activity meant the device idle timer (300s) could still fire before the
next keepalive in low-activity scenarios.

Fix: keepalive interval reduced to 30s and keepalive loop runs unconditionally.
"""

from mocks.clock import MockClock
from mocks.mock_device import MockDevice
from mocks.rti_driver import RTIDriver


def test_bug_001_no_idle_disconnect_after_5_minutes():
    clock = MockClock()
    device = MockDevice(reachable=True, idle_timeout=300, clock=clock)
    driver = RTIDriver(device)
    driver.connect()

    for _ in range(10):  # 10 x 30s = 5 minutes
        clock.advance(30)
        driver.keepalive()

    assert driver.status == "Online"
    assert driver.power_on() is True


def test_bug_001_no_idle_disconnect_after_30_minutes():
    clock = MockClock()
    device = MockDevice(reachable=True, idle_timeout=300, clock=clock)
    driver = RTIDriver(device)
    driver.connect()

    for _ in range(60):  # 60 x 30s = 30 minutes
        clock.advance(30)
        driver.keepalive()

    assert driver.status == "Online"
