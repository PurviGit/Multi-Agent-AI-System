# main.py
import os
from classifier_agent.classifier import ClassifierAgent
from shared_memory.memory import SharedMemory
from json_agent.json_agent import JSONAgent
from email_agent.email_agent import EmailAgent

# Initialize shared memory
memory = SharedMemory()

# Initialize agents
classifier = ClassifierAgent(memory)
json_agent = JSONAgent(memory)
email_agent = EmailAgent(memory)

# Simulate input files
input_files = [
    "samples/email_sample.txt",
    "samples/invoice_sample.json"
]

# Process each input
for file_path in input_files:
    format_type, intent = classifier.classify(file_path)

    if format_type == "JSON":
        json_agent.process(file_path)
    elif format_type == "Email":
        with open(file_path, 'r') as f:
            content = f.read()
        email_agent.process(content)
    else:
        print(f"[Main] No agent available for format: {format_type}")

print("\n[Shared Memory Snapshot]")
for entry in memory.memory_log:
    print(entry)
