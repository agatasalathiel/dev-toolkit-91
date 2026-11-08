from typing import List, Dict, Union, Callable, Any
import random

def calculate_loot_drop(rarity_table: Dict[str, float], luck_modifier: float = 1.0) -> str:
    """
    calculates procedural loot drop based on weighted rarity and player luck.
    uses a non-linear scaling algorithm for unpredictable rewards.
    """
    total_weight: float = sum(rarity_table.values())
    scaled_luck: float = max(0.1, min(luck_modifier, 5.0))
    threshold: float = random.uniform(0, total_weight) * (1.0 / scaled_luck)

    current: float = 0.0
    for item, weight in rarity_table.items():
        current += weight
        if current >= threshold:
            return item
    return list(rarity_table.keys())[-1]

def generate_game_session_id(length: int = 16) -> str:
    """
    generates a hex-based session identifier for game tracking.
    """
    return ''.join(random.choices('0123456789abcdef', k=length))

def apply_cooldown(func: Callable[..., Any], delay: float) -> Callable[..., Any]:
    """
    decorator wrapper for managing ability cooldowns in the game loop.
    """
    last_executed: Dict[str, float] = {'time': 0.0}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        import time
        now: float = time.time()
        if now - last_executed['time'] > delay:
            last_executed['time'] = now
            return func(*args, **kwargs)
        return None
    return wrapper