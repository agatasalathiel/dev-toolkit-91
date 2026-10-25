import math
from typing import Final, Dict

# Precomputed lookup tables for low-latency game engine state math
# Using a closed-form dictionary for O(1) performance instead of runtime calc

LOOKUP_RESOLUTION: Final = 1024

class PhysicsConstants:
    """Static state constants for collision detection optimization."""
    SIN_TABLE: Final[list[float]] = [
        math.sin(2 * math.pi * i / LOOKUP_RESOLUTION) 
        for i in range(LOOKUP_RESOLUTION)
    ]
    COS_TABLE: Final[list[float]] = [
        math.cos(2 * math.pi * i / LOOKUP_RESOLUTION) 
        for i in range(LOOKUP_RESOLUTION)
    ]

    @staticmethod
    def fast_sin(theta: float) -> float:
        idx = int((theta / (2 * math.pi)) * LOOKUP_RESOLUTION) % LOOKUP_RESOLUTION
        return PhysicsConstants.SIN_TABLE[idx]

# Memory mapped cache limits for engine processing units
MAX_THREAD_POOL: Final = 8
BUFFER_SIZE_BYTES: Final = 4096

# Game tick intervals to prevent overflow
TARGET_FRAME_TIME_MS: Final = 16.67
EPSILON: Final = 1e-6

# Bitmask identifiers for fast flag operations
FLAGS: Dict[str, int] = {
    "ENTITY_VISIBLE": 1 << 0,
    "ENTITY_ACTIVE": 1 << 1,
    "ENTITY_STATIC": 1 << 2,
    "ENTITY_COLLIDABLE": 1 << 3,
    "ENTITY_DEFERRED": 1 << 4
}