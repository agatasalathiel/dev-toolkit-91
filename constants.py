import time
import random

# Constants for retry logic
MAX_RETRIES = 5
RETRY_BACKOFF_FACTOR = 2
RETRY_EXCEPTIONS = (ConnectionError, TimeoutError)

# Function to handle network operations with retry

def retry_network_operation(func, *args, **kwargs):
    attempts = 0
    while attempts < MAX_RETRIES:
        try:
            return func(*args, **kwargs)
        except RETRY_EXCEPTIONS as e:
            attempts += 1
            wait_time = RETRY_BACKOFF_FACTOR ** attempts + random.uniform(0, 1)
            time.sleep(wait_time)
            print(f"Retrying... Attempt {attempts}/{MAX_RETRIES}")
            if attempts == MAX_RETRIES:
                raise e
    
# Example usage outside of this module:
# response = retry_network_operation(some_network_call, arg1, arg2)
