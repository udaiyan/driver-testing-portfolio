# Mock Driver

## What it does
Simulates connecting to an AV device over IP, sending commands, and reporting status.

## Files
| File | Purpose |
|---|---|
| `mocks/mock_device.py` | Simulated AV device |
| `mocks/base_driver.py` | Shared driver logic |
| `mocks/control4_driver.py` | Control4 variant |
| `mocks/rti_driver.py` | RTI variant |
| `mocks/crestron_driver.py` | Crestron variant |
| `mocks/control4/mock_driver.lua` | Illustrative DriverWorks driver |

## How to run
```bash
pip install -r requirements.txt
pytest -v
```

## How to extend
- Add new commands to MockDevice._handle
- Add a new platform subclass with its own keepalive rules
- Add a new test case in manual-tests/test-cases/


### `docs/installer-guide.md`

# Installer Guide — Mock AV Driver

## Before you start
- Driver file available
- Device reachable on the network
- IP address and port noted

## Step 1 - Add the driver
1. Open the project.
2. Add the mock driver.
3. Save.

## Step 2 - Configure
1. Set **IP** to the device address (e.g. `192.168.1.50`).
2. Set **Port** to `5000`.
3. Apply.

## Step 3 - Verify
- Status should show **Online**.
- Send **Power On** — device should respond.

## Step 4 - Troubleshooting
See [KB: Control4 offline driver](kb-troubleshooting-control4.md).

## Support
If the driver stays Offline, collect:
- Driver version
- Device model
- IP and port
- Driver logs