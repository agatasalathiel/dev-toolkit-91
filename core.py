from typing import Dict, List, Generator

class SpatialHashGrid:
    """Bit-packed spatial partitioning grid for ultra-fast gaming entity updates."""
    __slots__ = ('cell_size', '_grid', '_entity_cells')

    def __init__(self, cell_size: float = 64.0):
        self.cell_size = cell_size
        self._grid: Dict[int, List[int]] = {}
        self._entity_cells: Dict[int, int] = {}

    def _hash(self, x: float, y: float) -> int:
        cx = int(x // self.cell_size) & 0xFFFF
        cy = int(y // self.cell_size) & 0xFFFF
        return (cx << 16) | cy

    def update_entity(self, entity_id: int, x: float, y: float) -> bool:
        cell_key = self._hash(x, y)
        old_key = self._entity_cells.get(entity_id)

        if old_key == cell_key:
            return False

        if old_key is not None and old_key in self._grid:
            bucket = self._grid[old_key]
            if entity_id in bucket:
                bucket.remove(entity_id)
            if not bucket:
                del self._grid[old_key]

        self._entity_cells[entity_id] = cell_key
        self._grid.setdefault(cell_key, []).append(entity_id)
        return True

    def query_radius(self, x: float, y: float, radius: float) -> Generator[int, None, None]:
        min_cx = int((x - radius) // self.cell_size)
        max_cx = int((x + radius) // self.cell_size)
        min_cy = int((y - radius) // self.cell_size)
        max_cy = int((y + radius) // self.cell_size)

        for cx in range(min_cx, max_cx + 1):
            for cy in range(min_cy, max_cy + 1):
                key = ((cx & 0xFFFF) << 16) | (cy & 0xFFFF)
                if key in self._grid:
                    yield from self._grid[key]

    def clear(self) -> None:
        self._grid.clear()
        self._entity_cells.clear()
