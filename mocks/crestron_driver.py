from mocks.base_driver import BaseDriver


class CrestronDriver(BaseDriver):
    """Mock Crestron SIMPL-wrapper driver."""

    platform = "Crestron"
    keepalive_interval = 30
