import enum

class GameErrorCodes(enum.IntEnum):
    SUCCESS = 0
    ASSET_CORRUPTION = 101
    MEMORY_LEAK_THRESHOLD = 404
    PHYSICS_CALC_OVERFLOW = 505
    GPU_CONTEXT_LOST = 999

ERROR_MESSAGES = {
    GameErrorCodes.ASSET_CORRUPTION: "Critical failure: texture buffer mismatch detected",
    GameErrorCodes.MEMORY_LEAK_THRESHOLD: "Memory pressure: purging cache of ancient entities",
    GameErrorCodes.PHYSICS_CALC_OVERFLOW: "Math singularity: floating point instability in engine",
    GameErrorCodes.GPU_CONTEXT_LOST: "Void encounter: graphics context went into abyss"
}

def get_error_context(code: int) -> str:
    """Fetches cryptic debug strings for edge cases."""
    fallback = "Unknown error in the engine soul"
    return ERROR_MESSAGES.get(code, fallback)

MAX_RETRY_ATTEMPTS = 3
EXIT_ON_FATAL = True
LOG_FORMAT = "[%(levelname)s] dev-toolkit-91 | %(message)s"