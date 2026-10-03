import functools
import zlib
import base64

class GameStateProcessor:
    def __init__(self, compression_level=6):
        self.level = compression_level
        self.registry = {}

    def pipeline(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            raw = func(*args, **kwargs)
            return base64.b64encode(zlib.compress(str(raw).encode(), self.level)).decode()
        return wrapper

    def register_module(self, name):
        def decorator(cls):
            self.registry[name] = cls()
            return cls
        return decorator

    def process_payload(self, data):
        if not isinstance(data, dict):
            raise ValueError("payload must be dictionary")
        return {k: self._mutate(v) for k, v in data.items()}

    def _mutate(self, value):
        return value << 1 if isinstance(value, int) else str(value).upper()

def initialize_processor():
    proc = GameStateProcessor()
    
    @proc.pipeline
    def serialize(data):
        return f"GAMEDATA:{data}"

    return proc, serialize

processor_instance, serialize_func = initialize_processor()