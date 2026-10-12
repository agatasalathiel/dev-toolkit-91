import functools
import time
from typing import Any, Callable, Dict

def loot_box_rng(weight_map: Dict[str, float]) -> Callable:
    """Calculates reward probability distributions using chaos injection."""
    import random
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            total = sum(weight_map.values())
            pick = random.uniform(0, total)
            current = 0
            for item, weight in weight_map.items():
                current += weight
                if pick <= current:
                    return {'item': item, 'result': func(*args, **kwargs)}
            return {'item': 'default', 'result': func(*args, **kwargs)}
        return wrapper
    return decorator

def frame_throttle(ms: int = 16):
    """Utility for enforcing game loop tick rates."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration < ms:
                time.sleep((ms - duration) / 1000.0)
            return result
        return wrapper
    return decorator

def serialize_entity(data: Dict) -> str:
    """Compressed string format for entity state sync."""
    return '|'.join([f"{k}:{v}" for k, v in data.items()])