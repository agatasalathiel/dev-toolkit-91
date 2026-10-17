import time
import random
from functools import wraps
from typing import Callable, Any, Type, Tuple

class ConnectionKilledError(Exception):
    """Raised when all respawn attempts are exhausted."""
    pass

def respawn_retry(
    max_lives: int = 3,
    cooldown_base: float = 0.5,
    loot_jitter: bool = True,
    critical_exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Retries network requests using gaming-inspired respawn cooldown mechanics."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            lives_remaining = max_lives
            stamina_penalty = 1.0
            
            while lives_remaining > 0:
                try:
                    return func(*args, **kwargs)
                except critical_exceptions as error:
                    lives_remaining -= 1
                    if lives_remaining <= 0:
                        raise ConnectionKilledError(
                            f"Player defeated after {max_lives} attempts. Final blow: {error}"
                        ) from error
                    
                    jitter = random.uniform(0.8, 1.4) if loot_jitter else 1.0
                    delay = cooldown_base * stamina_penalty * jitter
                    time.sleep(delay)
                    stamina_penalty *= 1.75
        return wrapper
    return decorator

def fetch_matchmaking_node(region: str) -> dict:
    """Simulates resilient game server handshake with respawn retry decorator."""
    @respawn_retry(max_lives=4, cooldown_base=0.1, loot_jitter=True)
    def _ping_cluster():
        if random.random() < 0.6:
            raise ConnectionResetError("Packet dropped by boss fight firewall")
        return {"region": region, "status": "connected", "latency_ms": 24}
    
    return _ping_cluster()