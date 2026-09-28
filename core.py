from typing import Dict, List, Tuple

class BitwiseSpatialGrid:
    """High-performance 2D spatial partitioning using bit-packed integer keys."""
    
    def __init__(self, cell_size: int = 64, grid_width_bits: int = 16):
        self.cell_size = cell_size
        self.grid_width_bits = grid_width_bits
        self.mask = (1 << grid_width_bits) - 1
        self._cells: Dict[int, List[int]] = {}

    def _pack_coords(self, x: float, y: float) -> int:
        cx = max(0, int(x) // self.cell_size) & self.mask
        cy = max(0, int(y) // self.cell_size) & self.mask
        return (cx << self.grid_width_bits) | cy

    def clear(self) -> None:
        self._cells.clear()

    def insert(self, entity_id: int, x: float, y: float) -> int:
        key = self._pack_coords(x, y)
        if key not in self._cells:
            self._cells[key] = []
        self._cells[key].append(entity_id)
        return key

    def get_nearby(self, x: float, y: float, radius: float) -> List[int]:
        min_x = max(0, int(x - radius)) // self.cell_size
        max_x = max(0, int(x + radius)) // self.cell_size
        min_y = max(0, int(y - radius)) // self.cell_size
        max_y = max(0, int(y + radius)) // self.cell_size

        nearby: List[int] = []
        for cx in range(min_x, max_x + 1):
            for cy in range(min_y, max_y + 1):
                key = ((cx & self.mask) << self.grid_width_bits) | (cy & self.mask)
                if key in self._cells:
                    nearby.extend(self._cells[key])
        return nearby

    def optimize_density(self) -> Dict[str, float]:
        total_items = sum(len(v) for v in self._cells.values())
        total_cells = len(self._cells) or 1
        return {
            "cell_count": float(total_cells),
            "avg_density": total_items / total_cells,
            "allocated_keys": float(len(self._cells.keys()))
        }
