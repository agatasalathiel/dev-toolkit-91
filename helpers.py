"""Gaming helper utilities for dynamic stat modifier chains and experience scaling."""

from dataclasses import dataclass
from functools import reduce
import math
from typing import Callable, Generator, Tuple, TypeVar

T = TypeVar("T", int, float)
StatModifier = Callable[[float], float]


@dataclass(frozen=True)
class StatChain:
    """Immutable pipeline of stat modifiers evaluated sequentially via operator overloading."""

    base_value: float
    modifiers: Tuple[StatModifier, ...] = ()

    def __add__(self, modifier: StatModifier) -> "StatChain":
        """Appends a modifier function into the chain using the addition operator."""
        return StatChain(self.base_value, self.modifiers + (modifier,))

    def resolve(self) -> float:
        """Evaluates the entire chain and returns the final calculated attribute value."""
        return reduce(lambda val, mod: mod(val), self.modifiers, self.base_value)


def build_buff_multiplier(percent: float) -> StatModifier:
    """Creates a percentage-based scaling modifier for game entity attributes."""
    return lambda value: value * (1.0 + percent / 100.0)


def calculate_experience_curve(
    target_level: int,
    base_xp: int = 100,
    exponent: float = 1.5
) -> Generator[Tuple[int, int], None, None]:
    """Yields level milestone and cumulative experience points required up to target level."""
    accumulated_xp = 0
    for current_lvl in range(1, target_level + 1):
        required = math.floor(base_xp * (current_lvl ** exponent))
        accumulated_xp += required
        yield current_lvl, accumulated_xp
