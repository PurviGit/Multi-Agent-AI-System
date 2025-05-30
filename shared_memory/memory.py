# shared_memory/memory.py
from datetime import datetime

class SharedMemory:
    def __init__(self):
        self.memory_log = []

    def log(self, entry):
        self.memory_log.append(entry)
        print(f"[LOGGED] {entry}")

    def get_latest(self):
        return self.memory_log[-1] if self.memory_log else None

    def search_by_intent(self, intent):
        return [entry for entry in self.memory_log if entry.get("intent") == intent]

    def search_by_format(self, format_type):
        return [entry for entry in self.memory_log if entry.get("format") == format_type]
