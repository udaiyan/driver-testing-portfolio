def test_rti_end_to_end(rti_driver, clock):
    assert rti_driver.connect() == "Online"
    assert rti_driver.power_on() is True

    for _ in range(20):
        clock.advance(30)
        rti_driver.keepalive()

    assert rti_driver.status == "Online"
