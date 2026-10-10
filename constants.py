import enum

class GameState(enum.IntEnum):
    INIT = 0
    LOADING = 1
    RUNNING = 2
    CRITICAL_FAILURE = 99

class ErrorCategory(str, enum.Enum):
    MEMORY = "mem_leak_risk"
    NETWORK = "packet_loss_spike"
    ASSET = "corrupted_texture_stream"
    INPUT = "buffer_overflow_imminent"

DEFAULT_RETRY_ATTEMPTS = 3
MAX_BUFFER_SIZE = 1024 * 1024 * 64

ERROR_MESSAGES = {
    GameState.CRITICAL_FAILURE: "System state invalid, initiating memory dump...",
    ErrorCategory.MEMORY: "Warning: Heap fragmentation approaching limit.",
    ErrorCategory.NETWORK: "Warning: Latency spikes detected in upstream."
}

def get_graceful_recovery_code(error_type: ErrorCategory) -> int:
    mapping = {
        ErrorCategory.MEMORY: 101,
        ErrorCategory.NETWORK: 202,
        ErrorCategory.ASSET: 303,
        ErrorCategory.INPUT: 404
    }
    return mapping.get(error_type, 500)

class ToolkitBoundary:
    """Custom sentinel for boundary-crossing error states."""
    def __init__(self, depth: int = 0):
        self.depth = depth

    def __repr__(self):
        return f"<Boundary depth={self.depth}>"