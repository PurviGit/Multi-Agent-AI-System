# Multi-Agent AI System

## Objective

A multi-agent AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, and routes it to the appropriate agent. The system maintains shared context (e.g., sender, topic, last extracted fields) to enable chaining and traceability.

---

## Agents Overview

### 1. Classifier Agent

- **Input:** Raw file (PDF, JSON, or Email text file)
- **Function:** Classifies format and intent, routes to appropriate agent, logs to shared memory

### 2. JSON Agent

- **Input:** JSON payload
- **Function:** Extracts and validates fields, flags missing data, reformats for storage

### 3. Email Agent

- **Input:** Plain text email
- **Function:** Extracts sender, intent, urgency, and formats into CRM-style logs

### Shared Memory Module

- Stores:
  - File source, type, timestamp
  - Extracted values
  - Agent outputs
  - Conversation/thread ID (if extended)

---

## Tech Stack

- Python 3.8+
- LLM-ready design (optional)
- In-memory shared store (no DB needed)

---

## Project Structure
