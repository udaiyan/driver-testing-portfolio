from mocks.base_driver import BaseDriver


class RTIDriver(BaseDriver):
    """Mock RTI two-way driver (RS-232/IP)."""

    platform = "RTI"
    keepalive_interval = 30  # Fixed: was 60s; device idle timeout is 300s
