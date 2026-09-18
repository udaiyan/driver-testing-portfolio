"""Simulated AV device. No real hardware required."""

from mocks.clock import MockClock


class MockDevice:
    def __init__(
        self,
        ip="192.168.1.50",
        port=5000,
        reachable=True,
        idle_timeout=300,
        clock=None,
    ):
        self.ip = ip
        self.port = port
        self.reachable = reachable
        self.idle_timeout = idle_timeout
        self.clock = clock or MockClock()
        self.power = False
        self.volume = 50
        self.input = "HDMI1"
        self._last_command = self.clock.time()
        self.command_log = []

    def ping(self):
        return self.reachable

    def send(self, command):
        self.command_log.append(command)

        if not self.reachable:
            raise TimeoutError(f"No response from {self.ip}:{self.port}")

        if self.clock.time() - self._last_command > self.idle_timeout:
            raise TimeoutError("Idle timeout")

        self._last_command = self.clock.time()
        return self._handle(command)

    def _handle(self, command):
        if command == "POWER_ON":
            self.power = True
            return "OK POWER_ON"
        if command == "POWER_OFF":
            self.power = False
            return "OK POWER_OFF"
        if command == "STATUS":
            return f"OK POWER={'ON' if self.power else 'OFF'}"
        if command.startswith("VOLUME "):
            self.volume = int(command.split()[1])
            return f"OK VOLUME {self.volume}"
        return "ERR UNKNOWN_COMMAND"
