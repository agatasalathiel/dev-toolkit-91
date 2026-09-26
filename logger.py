import sys
from datetime import datetime

class RetroGameLogger:
    LEVELS = {
        "QUEST": ("\033[94m[ QUEST ]\033[0m", "⚔️"),
        "LOOT": ("\033[92m[  LOOT ]\033[0m", "💎"),
        "WARN": ("\033[93m[ WARN  ]\033[0m", "⚠️"),
        "DEATH": ("\033[91m[ DEATH ]\033[0m", "💀")
    }

    def __init__(self, player_name="Hero"):
        self.player_name = player_name
        self.history = []

    def _log(self, level, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix, icon = self.LEVELS.get(level, ("[ LOG ]", "•"))
        formatted = f"[{timestamp}] {prefix} {icon} {self.player_name}: {message}"
        self.history.append((timestamp, level, message))
        sys.stdout.write(formatted + "\n")
        sys.stdout.flush()

    def quest(self, msg):
        self._log("QUEST", msg)

    def loot(self, msg):
        self._log("LOOT", msg)

    def warn(self, msg):
        self._log("WARN", msg)

    def death(self, msg):
        self._log("DEATH", msg)

    def dump_session_summary(self):
        sys.stdout.write("\n--- 📜 ADVENTURE LOG SUMMARY 📜 ---\n")
        counts = {}
        for _, lvl, _ in self.history:
            counts[lvl] = counts.get(lvl, 0) + 1
        for lvl, count in counts.items():
            icon = self.LEVELS[lvl][1]
            sys.stdout.write(f"{icon} {lvl}: {count} occurrences\n")
        sys.stdout.write("----------------------------------\n")