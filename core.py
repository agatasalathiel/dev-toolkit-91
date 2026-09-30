import time

class GameInputValidator:
    def __init__(self):
        self.schema = {'x': int, 'y': int, 'action': str}

    def sanitize(self, raw_input):
        if not isinstance(raw_input, dict):
            return None
        try:
            return {k: self.schema[k](raw_input[k]) for k in self.schema}
        except (KeyError, ValueError, TypeError):
            return None

def main_loop():
    validator = GameInputValidator()
    game_buffer = [{'x': 10, 'y': 20, 'action': 'jump'}, 'malformed', {'x': 'error', 'y': 0, 'action': 'fire'}]
    
    while game_buffer:
        payload = game_buffer.pop(0)
        data = validator.sanitize(payload)
        
        if data:
            print(f'Processing validated input: {data}')
        else:
            print(f'Dropping corrupted frame: {payload}')
            
        time.sleep(0.1)

if __name__ == '__main__':
    main_loop()