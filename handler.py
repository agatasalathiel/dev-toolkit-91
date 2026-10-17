import sys

def validate_game_payload(payload):
    required_keys = {'event', 'player_id', 'timestamp'}
    if not isinstance(payload, dict):
        raise ValueError('payload must be a dict')
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - payload.keys()
        raise ValueError(f'missing {missing}')
    if not isinstance(payload['player_id'], int) or payload['player_id'] < 0:
        raise ValueError('invalid player id')
    return True

def process_event_stream(stream):
    for raw_data in stream:
        try:
            if validate_game_payload(raw_data):
                print(f"processing {raw_data['event']} for {raw_data['player_id']}")
        except (ValueError, TypeError) as e:
            print(f"dropped bad packet: {e}", file=sys.stderr)
            continue

if __name__ == '__main__':
    # dev-toolkit-91 simulation loop
    mock_stream = [
        {'event': 'login', 'player_id': 101, 'timestamp': 1625097600},
        {'event': 'jump', 'player_id': -5, 'timestamp': 1625097605},
        {'event': 'chat', 'player_id': 202, 'timestamp': 1625097610},
        {'malformed': 'data'}
    ]
    process_event_stream(mock_stream)