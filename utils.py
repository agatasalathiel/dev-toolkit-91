"""Gaming data handling utility for compact state serialization and stat calculations."""
from typing import List, Tuple, Dict, Union
import math


class BitPackedInventory:
    """Serializes grid-based item coordinates into compact binary representations."""

    def __init__(self, grid_size: Tuple[int, int] = (8, 8)):
        self.cols, self.rows = grid_size
        self.max_bits = self.cols * self.rows

    def encode_occupancy(self, occupied_cells: List[Tuple[int, int]]) -> str:
        mask = 0
        for r, c in occupied_cells:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                bit_index = r * self.cols + c
                mask |= (1 << bit_index)
        byte_len = (self.max_bits + 7) // 8
        return mask.to_bytes(byte_len, byteorder="big").hex()

    def decode_occupancy(self, hex_string: str) -> List[Tuple[int, int]]:
        data = bytes.fromhex(hex_string)
        mask = int.from_bytes(data, byteorder="big")
        cells = []
        for bit_index in range(self.max_bits):
            if (mask >> bit_index) & 1:
                r = bit_index // self.cols
                c = bit_index % self.cols
                cells.append((r, c))
        return cells


def dynamic_stat_scaler(base_stats: Dict[str, float], level: int, variance: float = 0.05) -> Dict[str, float]:
    """Scales entity base stats logarithmically with deterministic mathematical variance."""
    scaled = {}
    for stat, base in base_stats.items():
        seed = sum(ord(ch) for ch in stat) + level
        pseudo_rnd = (math.sin(seed) * 10000) - math.floor(math.sin(seed) * 10000)
        factor = 1 + (math.log(level + 1) * 0.55) + ((pseudo_rnd - 0.5) * variance)
        scaled[stat] = round(base * max(0.1, factor), 2)
    return scaled
