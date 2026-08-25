import datetime
from collections import defaultdict

class GameLogger:
    def __init__(self, session_name="dev_toolkit_game"):
        self.session_name = session_name
        self.events = []
        self.counters = defaultdict(int)

    def _get_timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def record_event(self, event_type, description, data=None):
        timestamp = self._get_timestamp()
        entry = {
            "time": timestamp,
            "type": event_type,
            "desc": description,
            "data": data or {}
        }
        self.events.append(entry)
        self.counters[event_type] += 1
        flavor = "⚔️" if event_type == "combat" else "🧭" if event_type == "explore" else "📜"
        print(f"{flavor} [{timestamp}] {event_type}: {description}")
        if data:
            print("   Details:", data)

    def log_combat(self, player, enemy, outcome):
        self.record_event("combat", f"{player} vs {enemy}", {"outcome": outcome})
    def log_quest_progress(self, quest, progress):
        self.record_event("quest", f"Quest: {quest}", {"progress": progress})
    def log_player_level(self, player, level):
        self.record_event("level", f"{player} reached level {level}")

    def get_stats(self):
        return dict(self.counters)

    def export_journal(self):
        return {
            "session": self.session_name,
            "events": self.events,
            "summary": self.get_stats()
        }

    def reset(self):
        self.events = []
        self.counters.clear()

if __name__ == "__main__":
    logger = GameLogger("test_session")
    logger.log_combat("Hero", "Dragon", "victory")
    logger.log_quest_progress("Slay the dragon", 100)
    logger.log_player_level("Hero", 5)
    print("Stats:", logger.get_stats())
    journal = logger.export_journal()
    print("Journal session:", journal["session"])