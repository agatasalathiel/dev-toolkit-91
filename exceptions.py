from typing import Optional, Any

class ToolkitError(Exception):
    """Base exception for the dev-toolkit-91 framework."""
    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        self.context = context or {}
        super().__init__(f"{message} | Context: {self.context}")

class GamingLogicError(ToolkitError):
    """Raised when game state transitions reach invalid paths."""
    pass

class ResourceManifestError(ToolkitError):
    """Raised when external game assets fail validation."""
    pass

def raise_with_context(exception_type: type[ToolkitError], msg: str, **kwargs: Any) -> None:
    """Dynamic instantiation of toolkit exceptions with arbitrary kwargs."""
    raise exception_type(msg, context=kwargs)

class StateTransitionFailure(GamingLogicError):
    """Specific error for failed tick updates in engine."""
    def __init__(self, tick: int, reason: str) -> None:
        super().__init__(f"Tick {tick} failed", {"reason": reason, "tick": tick})