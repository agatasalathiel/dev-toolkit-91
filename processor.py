import inspect
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, TypeVar

T = TypeVar("T")

@dataclass
class Entity:
    id: str
    hp: int = 100
    stamina: int = 100
    tags: List[str] = field(default_factory=list)

class EventProcessor:
    """Dynamic pipeline processor for gaming entity events using functional dispatches."""
    
    def __init__(self) -> None:
        self._registry: Dict[str, List[Callable[[Entity, Dict[str, Any]], None]]] = {}

    def register(self, event_type: str):
        def decorator(fn: Callable[[Entity, Dict[str, Any]], None]):
            self._registry.setdefault(event_type, []).append(fn)
            return fn
        return decorator

    def dispatch(self, event_type: str, entity: Entity, payload: Dict[str, Any]) -> Entity:
        handlers = self._registry.get(event_type, [])
        for handler in handlers:
            handler(entity, payload)
        return entity

    def purge_dead_entities(self, entities: List[Entity]) -> List[Entity]:
        return [e for e in entities if e.hp > 0 and "ghost" not in e.tags]

processor = EventProcessor()

@processor.register("damage")
def _apply_damage(entity: Entity, payload: Dict[str, Any]) -> None:
    amount = payload.get("amount", 0)
    entity.hp = max(0, entity.hp - amount)
    if entity.hp == 0:
        entity.tags.append("dead")

@processor.register("heal")
def _apply_heal(entity: Entity, payload: Dict[str, Any]) -> None:
    if "dead" not in entity.tags:
        entity.hp = min(100, entity.hp + payload.get("amount", 0))

def execute_tick(entities: List[Entity], events: List[tuple]) -> List[Entity]:
    for event_type, target_id, data in events:
        target = next((e for e in entities if e.id == target_id), None)
        if target:
            processor.dispatch(event_type, target, data)
    return processor.purge_dead_entities(entities)