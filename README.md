# 🤖 Customer Service Chatbot (LLM + Local Knowledge Base)

A hybrid AI-powered customer service chatbot built in Python, combining:

- ✅ **Local intent-based responses** for fast, common queries
- 🧠 **LLM-powered answers** using Together AI's streaming API for advanced questions

Perfect for e-commerce platforms looking to automate support using natural, human-like conversation.

---

## 🛠️ Features

- 🔍 Local keyword-matching for instant responses
- 🧠 Uses `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free` via Together API
- 💬 Streams replies token by token like real typing
- 📦 Covers:
  - Order Tracking
  - Returns & Refunds
  - Store Hours
  - Contact Info
  - General Inquiries
- 🔐 Easily plug in your own Together API key

---

## 📦 Requirements

- Python 3.8+
- Together API key (get yours at [http://api.together.ai](https://api.together.ai/))

---

## 🔧 Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-repo/customer-service-chatbot
cd customer-service-chatbot
