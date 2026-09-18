from mocks.control4_driver import Control4Driver


def test_driver_online_when_device_reachable(control4_driver):
    assert control4_driver.connect() == "Online"


def test_driver_offline_when_device_unreachable(offline_device):
    driver = Control4Driver(offline_device)
    assert driver.connect() == "Offline"


def test_disconnect_sets_status_offline(control4_driver):
    control4_driver.connect()
    control4_driver.disconnect()
    assert control4_driver.status == "Offline"
