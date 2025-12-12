# Kasparro AI — Agentic Content Generation System  
### *By Rakshitha Valipireddy*

## 🚀 Overview

This repository contains my implementation of the **Kasparro Applied AI Engineer Challenge**, where the objective is to build a fully automated **multi-agent content generation system** using **LangChain** and **Groq LLaMA-3.3-70B**.

The system takes a single product JSON and generates:

- `faq.json`
- `product_page.json`
- `comparison_page.json`

All outputs follow strict, machine-readable JSON formats.

---

## 🧠 System Capabilities

- ✔ Multi-agent architecture  
- ✔ LangChain-based orchestration using `RunnableSequence`  
- ✔ `StructuredTool` agents with Pydantic schemas  
- ✔ Prompt-template-driven content generation  
- ✔ Reusable logic blocks for behaviors such as question generation, FAQ reasoning, comparison logic  
- ✔ Strict JSON-only LLM outputs  
- ✔ Modular, extensible design

---

## 🏗 Core Agents

| Agent | Responsibility |
|------|----------------|
| **parse_product** | Validates & normalizes raw product JSON |
| **generate_questions** | Generates 15 categorized customer questions |
| **build_faq** | Creates structured FAQ JSON using product + questions |
| **build_product_page** | Generates a JSON product description page |
| **build_comparison** | Builds fictional Product B + comparison JSON |

---

## 📁 Folder Structure

<img width="917" height="602" alt="image" src="https://github.com/user-attachments/assets/d357442d-c674-43ea-8303-05079e9c0664" />


---
## 📂 Output Files

All generated outputs are stored in:

output_langchain/
--├── faq.json
--├── product_page.json
--└── comparison_page.json

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```sh
git clone https://github.com/rak-shi/kasparro-ai-agentic-content-generation-system-Rakshitha_Valipireddy.git
cd kasparro-ai-agentic-content-generation-system-Rakshitha_Valipireddy

2️⃣ Create a virtual environment
py -3.11 -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add Groq API Key

Create .env:

GROQ_API_KEY=your_key_here

5️⃣ Run the pipeline
python main_langchain.py


Results will appear in:

output_langchain/

```



