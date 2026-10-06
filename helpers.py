import functools
import time

class memoize_with_expiry:
    def __init__(self, ttl=60):
        self.cache = {}
        self.ttl = ttl

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in self.cache:
                result, timestamp = self.cache[key]
                if now - timestamp < self.ttl:
                    return result
            result = func(*args, **kwargs)
            self.cache[key] = (result, now)
            return result
        return wrapper

def batch_process(data, chunk_size=1000):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def fast_flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

class PerformanceOptimizer:
    def __init__(self, threshold=0.01):
        self.threshold = threshold

    def profile_call(self, func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            res = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > self.threshold:
                print(f'Warning: {func.__name__} took {elapsed:.4f}s')
            return res
        return wrapper