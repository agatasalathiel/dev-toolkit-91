import traceback
from typing import Any, Dict, Optional


class GameEngineErrorRank:
    MINOR_GLITCH = "MINOR_GLITCH"
    GAME_BREAKING = "GAME_BREAKING"
    FATALITY = "FATALITY"


class ToolkitBaseException(Exception):
    """Base exception class for dev-toolkit-91 gaming engine."""

    def __init__(
        self,
        message: str,
        rank: str = GameEngineErrorRank.MINOR_GLITCH,
        context: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.rank = rank
        self.context = context or {}
        self.telemetry_dump = self._generate_telemetry()

    def _generate_telemetry(self) -> Dict[str, Any]:
        return {
            "error_type": self.__class__.__name__,
            "rank": self.rank,
            "details": self.message,
            "state_snapshot": self.context,
            "stack_depth": len(traceback.extract_stack()) - 2,
        }

    def format_diagnostic_hud(self) -> str:
        hud_lines = [
            f"=== [SYSTEM ALERT: {self.rank}] ===",
            f"Class: {self.__class__.__name__}",
            f"Reason: {self.message}",
        ]
        if self.context:
            hud_lines.append("Context Registry:")
            for k, v in self.context.items():
                hud_lines.append(f"  -> {k}: {v}")
        return "\n".join(hud_lines)


class SaveStateCorruptionError(ToolkitBaseException):
    """Raised when save files or game data blobs fail integrity checks."""

    def __init__(self, slot: int, payload_hash: str):
        super().__init__(
            message=f"Save payload at slot {slot} corrupt [hash={payload_hash[:8]}]",
            rank=GameEngineErrorRank.GAME_BREAKING,
            context={"slot": slot, "hash": payload_hash},
        )


class EntityNotFoundException(ToolkitBaseException):
    """Raised when an actor or entity ID cannot be resolved in the world grid."""

    def __init__(self, entity_id: str, coordinates: Optional[tuple] = None):
        super().__init__(
            message=f"Entity '{entity_id}' absent from world grid.",
            rank=GameEngineErrorRank.MINOR_GLITCH,
            context={"entity_id": entity_id, "coords": coordinates},
        )


class RenderPipelineGlitch(ToolkitBaseException):
    """Raised on GPU shading or vertex array bound failures."""

    def __init__(self, shader_stage: str, error_code: int):
        super().__init__(
            message=f"Pipeline failure during stage '{shader_stage}' (code {error_code})",
            rank=GameEngineErrorRank.FATALITY,
            context={"stage": shader_stage, "code": error_code},
        )
