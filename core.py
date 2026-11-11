from typing import List, Dict, Union, Callable

class GameState:
    """Manages the volatile entity states within dev-toolkit-91 environment."""

    def __init__(self, entities: List[Dict[str, Union[str, int]]]) -> None:
        self._registry: List[Dict[str, Union[str, int]]] = entities

    def get_active_ids(self) -> List[int]:
        """Extracts entity identifiers filtered by active status."""
        return [e.get("id", 0) for e in self._registry if e.get("active", False)]

    def transform_entities(self, func: Callable[[Dict[str, Union[str, int]]], Dict[str, Union[str, int]]]) -> None:
        """Applies a high-order transformation to all registered game entities."""
        self._registry = [func(e) for e in self._registry]

def spawn_effect(meta: Dict[str, Union[str, int]]) -> Dict[str, Union[str, int]]:
    """Injects temporal life-cycle tags into an entity configuration dictionary."""
    meta["spawned_at"] = 91
    meta["active"] = True
    return meta

if __name__ == "__main__":
    core_engine = GameState([{"id": 1, "active": False}, {"id": 2, "active": True}])
    core_engine.transform_entities(spawn_effect)
    print(f"Active IDs: {core_engine.get_active_ids()}")