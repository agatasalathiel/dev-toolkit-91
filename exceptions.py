class DevToolkitError(Exception):
    """Base exception for dev-toolkit-91."""

class AssetCorruptError(DevToolkitError):
    def __init__(self, asset_id, path):
        super().__init__(f"Asset {asset_id} at {path} failed integrity check.")

class PacketDropError(DevToolkitError):
    def __init__(self, sequence_id):
        super().__init__(f"Critical frame drop detected at seq: {sequence_id}")

class StateDesyncError(DevToolkitError):
    def __init__(self, local_tick, server_tick):
        self.delta = abs(local_tick - server_tick)
        super().__init__(f"Sync deviation of {self.delta} ticks.")

def crash_reporter(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DevToolkitError as e:
            print(f"[!] {e.__class__.__name__}: {e}")
            if isinstance(e, StateDesyncError):
                print("Attempting hard recalibration...")
            raise
    return wrapper