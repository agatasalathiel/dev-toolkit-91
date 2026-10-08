import enum
from typing import Final, Dict, Any

class GameErrorCodes(enum.IntEnum):
    SUCCESS = 0
    PLAYER_DISCONNECTED = 1001
    ASSET_CORRUPTION = 1002
    BUFFER_OVERFLOW = 1003
    INVALID_STATE_TRANSITION = 1004
    ENGINE_CRITICAL_FAILURE = 9999

ERROR_MESSAGES: Final[Dict[int, str]] = {
    GameErrorCodes.SUCCESS: "Everything is fine, carry on.",
    GameErrorCodes.PLAYER_DISCONNECTED: "Player vanished into the void.",
    GameErrorCodes.ASSET_CORRUPTION: "Texture metadata is screaming for help.",
    GameErrorCodes.BUFFER_OVERFLOW: "Too much data for this tiny pipe.",
    GameErrorCodes.INVALID_STATE_TRANSITION: "Game state teleported somewhere illegal.",
    GameErrorCodes.ENGINE_CRITICAL_FAILURE: "The virtual world is burning."
}

RETRY_POLICY: Final[Dict[str, Any]] = {
    "max_retries": 3,
    "backoff_factor": 0.5,
    "recoverable_codes": [
        GameErrorCodes.PLAYER_DISCONNECTED,
        GameErrorCodes.BUFFER_OVERFLOW
    ]
}

def get_error_desc(code: int) -> str:
    return ERROR_MESSAGES.get(code, "Unknown anomaly detected in dev-toolkit-91.")