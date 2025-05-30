# json_agent/json_agent.py
import json
from datetime import datetime

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

        required_fields = ["invoice_id", "customer", "total"]
        missing_fields = [field for field in required_fields if field not in data]

        processed = {
            "invoice_id": data.get("invoice_id"),
            "customer": data.get("customer"),
            "amount": data.get("total"),
            "status": "complete" if not missing_fields else "incomplete",
            "missing_fields": missing_fields,
            "timestamp": datetime.utcnow().isoformat()
        }

        print("[JSONAgent] Processed Data:", json.dumps(processed, indent=2))

        self.memory.log({
            "agent": "JSONAgent",
            "output": processed
        })
