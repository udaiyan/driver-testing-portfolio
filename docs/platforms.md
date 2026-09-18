# Platform Testing Notes

## Control4
- Tools: DriverEditor, Composer Pro
- Focus: DriverWorks/Lua drivers, IR testing
- Virtual option: Emulator drivers and simulators

## RTI
- Tools: Integration Designer, RTI SDK
- Focus: Two-way RS-232/IP drivers
- Virtual option: RTI Virtual Blu-ray, Virtual TV, Virtual Climate, Virtual Alarm

## Crestron
- Tools: SIMPL, XPanel, Drivers SDK Test Tools
- Focus: Platform-agnostic drivers
- Virtual option: XPanel simulator, third-party emulator drivers

## Automated coverage in this repo
Each platform has an integration test that exercises connect → power on → keepalive → power off.