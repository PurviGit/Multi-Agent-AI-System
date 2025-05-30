# classifier_agent/classifier.py
import json
import os
from datetime import datetime

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory

    def classify(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".json":
            file_format = "JSON"
            intent = self.detect_intent_json(file_path)
        elif ext == ".txt":
            file_format = "Email"
            intent = self.detect_intent_email(file_path)
        elif ext == ".pdf":
            file_format = "PDF"
            intent = self.detect_intent_pdf(file_path)
        else:
            file_format = "Unknown"
            intent = "Unknown"

        self.memory.log({
            "source": file_path,
            "format": file_format,
            "intent": intent,
            "timestamp": datetime.utcnow().isoformat()
        })

        return file_format, intent

    def detect_intent_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        if "invoice_id" in data:
            return "Invoice"
        elif "items" in data:
            return "RFQ"
        return "Unknown"

    def detect_intent_email(self, file_path):
        with open(file_path, 'r') as f:
            text = f.read().lower()
        if "complaint" in text:
            return "Complaint"
        elif "request for quote" in text or "rfq" in text:
            return "RFQ"
        return "Unknown"

    def detect_intent_pdf(self, file_path):
        # Placeholder: Assume PDFs are regulations for now
        return "Regulation"
