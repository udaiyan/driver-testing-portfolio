class MockClock:
    """Controllable clock so tests can fast-forward time."""

    def __init__(self, start=0.0):
        self._now = start

    def time(self):
        return self._now

    def advance(self, seconds):
        self._now += seconds
