from mocks.control4_driver import Control4Driver


def test_power_on_succeeds_when_online(control4_driver):
    control4_driver.connect()
    assert control4_driver.power_on() is True
    assert control4_driver.power is True


def test_power_off_after_power_on(control4_driver):
    control4_driver.connect()
    control4_driver.power_on()
    assert control4_driver.power_off() is True
    assert control4_driver.power is False


def test_power_on_fails_when_offline(offline_device):
    driver = Control4Driver(offline_device)
    driver.connect()
    assert driver.power_on() is False
    assert driver.status == "Offline"


def test_set_volume(control4_driver):
    control4_driver.connect()
    assert control4_driver.set_volume(35) is True
    assert control4_driver.volume == 35
