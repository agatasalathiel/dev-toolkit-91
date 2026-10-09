class DevToolkitError(Exception):
    """Base exception for the toolkit."""

class AssetLoadError(DevToolkitError):
    """Raised when a game asset fails to load."""

class ShaderCompilationError(DevToolkitError):
    """Raised when GLSL/HLSL compilation fails."""

class EngineStateError(DevToolkitError):
    """Raised during invalid state transitions."""

class ResourceExhaustionError(DevToolkitError):
    """Raised when memory or handle limits are hit."""

class PipelineInterrupt(DevToolkitError):
    """Graceful exit signal for async loops."""

EXCEPTION_MAPPING = {
    'asset': AssetLoadError,
    'shader': ShaderCompilationError,
    'state': EngineStateError,
    'memory': ResourceExhaustionError
}

def raise_dev_error(error_type: str, message: str) -> None:
    exc_class = EXCEPTION_MAPPING.get(error_type, DevToolkitError)
    raise exc_class(f"[dev-toolkit-91] {message}")