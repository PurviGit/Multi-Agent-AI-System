# Multi-Agent AI System

## 🎯 Objective

Build a multi-agent AI system that:

* Accepts input in **PDF, JSON, or Email (text)** format
* Classifies the **format and intent**
* Routes it to the **appropriate agent**
* Maintains a shared memory for context, chaining, and traceability

---

## 🧠 Architecture Overview

### 🧭 Classifier Agent

* **Input**: Raw file (email, JSON, or PDF)
* **Detects**: Format + Intent (Invoice, RFQ, Complaint, etc.)
* **Routes**: Sends data to Email Agent or JSON Agent
* **Logs**: Format and intent into Shared Memory

### 💾 Shared Memory Module

* Stores:

  * Source, format, intent, timestamp
  * Agent output and extracted values
* Implemented using an in-memory Python list (can be upgraded to Redis or SQLite)

### 📄 JSON Agent

* Accepts structured JSON payloads
* Extracts data into a unified schema
* Flags missing or anomalous fields

### 📧 Email Agent

* Parses raw email content
* Extracts sender, urgency, intent
* Formats data for CRM-like usage

---

## 🗂 Folder Structure

```
├── classifier_agent
│   └── classifier.py
├── email_agent
│   └── email_agent.py
├── json_agent
│   └── json_agent.py
├── shared_memory
│   └── memory.py
├── samples
│   ├── invoice_sample.json
│   └── email_sample.txt
├── main.py
├── README.md
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## ✅ Sample Output

```
[LOGGED] {'source': 'samples/email_sample.txt', 'format': 'Email', 'intent': 'RFQ'}
[EmailAgent] Processed Data: CRM_LOG | From: sales@acme.com | Intent: RFQ | Urgency: High
[LOGGED] {'agent': 'EmailAgent', 'output': {...}}

[LOGGED] {'source': 'samples/invoice_sample.json', 'format': 'JSON', 'intent': 'Invoice'}
[JSONAgent] Processed Data: {
  "invoice_id": "INV-2025-001",
  "customer": "ACME Corp",
  "amount": 1250.75,
  "status": "complete",
  "missing_fields": []
}
[LOGGED] {'agent': 'JSONAgent', 'output': {...}}
```

---

## 📁 Sample Input Files

### 🔹 `samples/email_sample.txt`

```
From: sales@acme.com
Subject: Urgent RFQ

Hi Team,
Please provide a quote for 500 units of product X.
Regards,
ACME Corp
```

### 🔹 `samples/invoice_sample.json`

```json
{
  "invoice_id": "INV-2025-001",
  "customer": "ACME Corp",
  "amount": 1250.75,
  "status": "complete"
}
```

---

## 📸 Screenshots 


![Screenshot 2025-05-30 183836](https://github.com/user-attachments/assets/76f7bb07-b8d9-42df-b7fa-7356416fe534)

---

## 📹 Submission Checklist

* [x] Working code with agents and memory
* [x] `samples/` folder with test files
* [x] `main.py` to demonstrate full pipeline
* [x] README.md with instructions and logs

---


## 🧑‍💻 Author

**Purvi** – Multi-Agent AI System Developer
