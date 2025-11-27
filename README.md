# Agent-for-good
Agent for students
# 🏆 Multi-Agent "Study Streamliner": An Adaptive LLM System for Verifiable Learning

## 🌟 Capstone Project: Concierge Agents Track

This project implements a sophisticated multi-agent system designed to automate the entire personalized learning lifecycle, from task planning to comprehensive knowledge evaluation.

---

## 💡 Problem & Value Proposition

### Problem Statement
Traditional LLM chatbots are unreliable for educational purposes due to factual inaccuracies (hallucination) and a complete lack of measurable evaluation. Relying on them for learning is inefficient and lacks accountability.

### Solution and Value
The Study Streamliner solves this by enforcing a sequential, quality-controlled workflow using specialized agents:

* **Accuracy & RAG:** The **Teacher Agent** integrates a **Google Search Tool** to ensure the lesson content is factual and up-to-date, transforming the LLM into a reliable Retrieval Augmented Generation (RAG) system.
* **Accountability:** The **Evaluator Agent** provides a measurable outcome (a score) and personalized feedback, verifying knowledge retention.
* **Compliance:** The system includes a robust **Compliance Offline Mode** for local development, while guaranteeing full functionality in the authenticated competition environment.

---

## ⚙️ Architecture and Agent Flow

The system operates as a **Sequential Multi-Agent System**, where agents collaborate by passing structured data (JSON) through a defined flow.

### 

### Agent Roles and Technical Features

| Agent (`.py` file) | Primary Responsibility | Key Technical Feature |
| :--- | :--- | :--- |
| **1. Planner Agent** (`planner_agent.py`) | **Task Decomposition.** Takes the user's goal (topic/difficulty) and produces a structured study outline. | **Structured Output (JSON Schema):** Enforces reliable A2A communication. |
| **2. Teacher Agent** (`teacher_agent.py`) | **Content Generation & Factual Retrieval.** Generates the detailed lesson based on the plan. | **Tool Use:** Integrates the **Google Search Tool** for RAG. |
| **3. Evaluator Agent** (`evaluator_agent.py`) | **Evaluation & Feedback.** Creates a 10-question quiz, collects answers interactively, and grades the submission locally. | **Robustness:** Includes **local grading logic** and **Compliance Offline Mode**. |

---

## 🛠️ Setup and Execution Instructions

### Prerequisites
1.  **Python 3.9+** installed.
2.  Clone this repository.

### Step 1: Setup Virtual Environment and Dependencies

Navigate to the project root directory and run:

```bash
# Create and activate the virtual environment
python -m venv venv
# Windows: .\venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
