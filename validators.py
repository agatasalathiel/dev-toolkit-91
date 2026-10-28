from typing import Dict, Any, Callable, List, Tuple

class BitmaskPacketValidator:
    """Validates binary game telemetry packets using custom bitwise schema masks."""

    def __init__(self, schema: List[Tuple[str, int, Callable[[int], bool]]]):
        self.schema = schema

    def validate_stream(self, raw_bytes: bytes) -> Dict[str, Any]:
        if not raw_bytes:
            raise ValueError("Empty telemetry payload")

        bit_string = "".join(f"{byte:08b}" for byte in raw_bytes)
        cursor = 0
        parsed_data: Dict[str, Any] = {}

        for field_name, bit_width, check_fn in self.schema:
            if cursor + bit_width > len(bit_string):
                raise ValueError(f"Packet overflow reading field '{field_name}'")

            raw_bits = bit_string[cursor : cursor + bit_width]
            value = int(raw_bits, 2)
            cursor += bit_width

            if not check_fn(value):
                raise ValueError(f"Validation failed for field '{field_name}' with value {value}")

            parsed_data[field_name] = value

        parsed_data["_remaining_bits"] = len(bit_string) - cursor
        return parsed_data


def validate_player_frame(raw_packet: bytes) -> Dict[str, Any]:
    """Validates a 32-bit compact player telemetry frame."""
    validator = BitmaskPacketValidator([
        ("player_id", 4, lambda val: 0 <= val <= 15),
        ("health", 8, lambda val: 0 <= val <= 100),
        ("pos_x", 12, lambda val: val <= 4000),
        ("action_flags", 8, lambda val: (val & 0b11000000) == 0)
    ])
    return validator.validate_stream(raw_packet)
