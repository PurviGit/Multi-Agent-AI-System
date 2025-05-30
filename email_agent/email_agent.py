# email_agent/email_agent.py
from datetime import datetime
import re

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, email_content):
        sender = self.extract_sender(email_content)
        urgency = self.detect_urgency(email_content)
        intent = self.detect_intent(email_content)

        processed = {
            "sender": sender,
            "intent": intent,
            "urgency": urgency,
            "formatted": f"CRM_LOG | From: {sender} | Intent: {intent} | Urgency: {urgency}",
            "timestamp": datetime.utcnow().isoformat()
        }

        print("[EmailAgent] Processed Data:", processed["formatted"])

        self.memory.log({
            "agent": "EmailAgent",
            "output": processed
        })

    def extract_sender(self, text):
        match = re.search(r"From: (.+?)\n", text, re.IGNORECASE)
        return match.group(1).strip() if match else "Unknown"

    def detect_urgency(self, text):
        if "urgent" in text.lower() or "asap" in text.lower():
            return "High"
        return "Normal"

    def detect_intent(self, text):
        if "complaint" in text.lower():
            return "Complaint"
        elif "rfq" in text.lower() or "request for quote" in text.lower():
            return "RFQ"
        elif "invoice" in text.lower():
            return "Invoice"
        return "Unknown"
