def test_unknown_command_returns_error(control4_driver):
    control4_driver.connect()
    response = control4_driver.device.send("FLY_TO_MOON")
    assert response == "ERR UNKNOWN_COMMAND"


def test_command_log_records_sent_commands(control4_driver):
    control4_driver.connect()
    control4_driver.power_on()
    assert "POWER_ON" in control4_driver.device.command_log
