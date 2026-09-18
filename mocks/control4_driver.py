from mocks.base_driver import BaseDriver


class Control4Driver(BaseDriver):
    """Mock DriverWorks-style driver for Control4."""

    platform = "Control4"
    keepalive_interval = 30
