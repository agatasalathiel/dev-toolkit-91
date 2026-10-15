from typing import Optional

class DevToolkitError(Exception):
    """Base exception for all dev-toolkit-91 operations."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(f"[{code}] {message}" if code else message)
        self.code = code

class AssetLoadError(DevToolkitError):
    """Raised when a game asset fails to load into memory."""
    pass

class ShaderCompilationError(DevToolkitError):
    """Raised when GLSL or HLSL compilation fails during runtime."""
    def __init__(self, log: str, stage: str = "unknown") -> None:
        super().__init__(f"Shader stage '{stage}' failed: {log}", 500)

class ConfigurationMismatchError(DevToolkitError):
    """Raised when local config conflicts with engine state."""
    pass

def raise_if_invalid(condition: bool, message: str, exception_class: type = DevToolkitError) -> None:
    """Guard clause utility for clean flow control in engine code."""
    if not condition:
        raise exception_class(message)