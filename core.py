import math
from array import array
from typing import List, Tuple

class BitpackedSpatialGrid:
    """High-performance spatial grid using bitfield packing for fast entity queries."""
    
    def __init__(self, width: int, height: int, cell_size: int = 32):
        self.cell_size = cell_size
        self.cols = math.ceil(width / cell_size)
        self.rows = math.ceil(height / cell_size)
        # Flattened grid stored in a C-style array of unsigned 32-bit integers
        self.grid_masks = array('I', [0] * (self.cols * self.rows))
        # Bit-shift factor calculated from power-of-two cell size
        self._cell_shift = max(1, cell_size.bit_length() - 1)

    def clear(self) -> None:
        """Reset grid state in-place without reallocation overhead."""
        for i in range(len(self.grid_masks)):
            self.grid_masks[i] = 0

    def register_entity(self, entity_id: int, x: float, y: float, category_bit: int) -> int:
        """Registers entity into grid cell using fast bitwise bitmask ORing."""
        col = int(x) >> self._cell_shift
        row = int(y) >> self._cell_shift
        
        if 0 <= col < self.cols and 0 <= row < self.rows:
            idx = row * self.cols + col
            self.grid_masks[idx] |= (1 << (category_bit & 31))
            return idx
        return -1

    def query_cell_mask(self, x: float, y: float) -> int:
        """Returns the raw category bitmask for a position in O(1) time."""
        col = int(x) >> self._cell_shift
        row = int(y) >> self._cell_shift
        
        if 0 <= col < self.cols and 0 <= row < self.rows:
            return self.grid_masks[row * self.cols + col]
        return 0

    def check_collision_layer(self, x: float, y: float, layer_bit: int) -> bool:
        """Bitwise test to verify if a target layer bit exists in the target cell."""
        return bool(self.query_cell_mask(x, y) & (1 << (layer_bit & 31)))
