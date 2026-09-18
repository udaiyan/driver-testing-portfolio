def test_crestron_end_to_end(crestron_driver, clock):
    assert crestron_driver.connect() == "Online"
    assert crestron_driver.power_on() is True

    for _ in range(20):
        clock.advance(30)
        crestron_driver.keepalive()

    assert crestron_driver.status == "Online"
