import time

RETRY_LIMIT = 5
RETRY_BACKOFF = 2

class NetworkRetries:
    def __init__(self, limit=RETRY_LIMIT, backoff=RETRY_BACKOFF):
        self.limit = limit
        self.backoff = backoff

    def retry(self, func, *args, **kwargs):
        attempts = 0
        while attempts < self.limit:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempts += 1
                if attempts >= self.limit:
                    raise e
                time.sleep(self.backoff ** attempts)


# Example usage of the retry logic:
if __name__ == '__main__':
    def dummy_network_call():
        raise ConnectionError('Unable to connect')  # Simulated failure

    network_retries = NetworkRetries()
    try:
        network_retries.retry(dummy_network_call)
    except Exception as error:
        print(f'Final error: {error}')