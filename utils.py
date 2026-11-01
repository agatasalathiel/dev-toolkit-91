import logging
import functools

logger = logging.getLogger('dev-toolkit-91')

class GameLogicError(Exception):
    pass

def robust_processor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, ValueError, IndexError, ZeroDivisionError) as e:
            logger.error(f'Edge case detected in {func.__name__}: {e}')
            return None
        except Exception as e:
            logger.critical(f'Unexpected critical state: {e}')
            raise GameLogicError('Fatal toolkit state corruption') from e
    return wrapper

@robust_processor
def calculate_hit_chance(raw_val, base_offset):
    # Protects against floating point precision and invalid input types
    if not isinstance(raw_val, (int, float)):
        raise ValueError('non-numeric hit data')
    return min(max(float(raw_val) + base_offset, 0.0), 1.0)

@robust_processor
def parse_entity_id(entity_string):
    # Handles malformed game entity strings
    return int(entity_string.split('_')[-1])

def safe_execute_task(task_queue, default_val=0):
    try:
        return task_queue.pop(0)
    except (AttributeError, IndexError):
        return default_val