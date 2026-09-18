"""Base driver with connection, keepalive and power control."""

import logging

from mocks.mock_device import MockDevice

log = logging.getLogger(__name__)


class BaseDriver:
    platform = "generic"
    keepalive_interval = 30  # seconds; must be < device idle timeout

    def __init__(self, device: MockDevice):
        self.device = device
        self.status = "Offline"
        self.power = False
        self.volume = 0
        self._last_keepalive = device.clock.time()

    def connect(self):
        log.info("Connecting to %s:%s", self.device.ip, self.device.port)
        if self.device.ping():
            self.status = "Online"
            log.info("Driver status: Online")
        else:
            self.status = "Offline"
            log.warning("Driver status: Offline (no response)")
        return self.status

    def disconnect(self):
        self.status = "Offline"
        log.info("Driver disconnected")

    def keepalive(self):
        if self.device.clock.time() - self._last_keepalive < self.keepalive_interval:
            return
        try:
            self.device.send("STATUS")
            self._last_keepalive = self.device.clock.time()
            log.info("Keepalive OK")
        except TimeoutError as exc:
            self.status = "Offline"
            log.warning("Keepalive failed: %s", exc)

    def _send(self, command):
        try:
            return self.device.send(command)
        except TimeoutError as exc:
            self.status = "Offline"
            log.error("Command %s failed: %s", command, exc)
            return None

    def power_on(self):
        if self._send("POWER_ON") == "OK POWER_ON":
            self.power = True
            return True
        return False

    def power_off(self):
        if self._send("POWER_OFF") == "OK POWER_OFF":
            self.power = False
            return True
        return False

    def set_volume(self, level):
        response = self._send(f"VOLUME {level}")
        if response and response.startswith("OK VOLUME"):
            self.volume = level
            return True
        return False
