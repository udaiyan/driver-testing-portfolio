# KB: RTI driver drops Offline after a while

## Symptoms
- Driver was Online but goes Offline after idle time.
- Commands fail until reconnect.

## Cause
Keepalive interval was too long relative to the device idle timeout.

## Fix (driver v0.2+)
- Keepalive interval reduced to 30s.
- Keepalive runs unconditionally.

## Verify
- Leave idle for 30 minutes.
- Send Power On — should succeed.

## If still failing
- Check `KEEPALIVE` setting in driver properties.
- Contact support with logs.