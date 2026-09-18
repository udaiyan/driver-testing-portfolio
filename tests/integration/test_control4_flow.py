def test_control4_end_to_end(control4_driver, clock):
    assert control4_driver.connect() == "Online"
    assert control4_driver.power_on() is True

    for _ in range(20):
        clock.advance(30)
        control4_driver.keepalive()

    assert control4_driver.status == "Online"
    assert control4_driver.set_volume(20) is True
    assert control4_driver.power_off() is True
