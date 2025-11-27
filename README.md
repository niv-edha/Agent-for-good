# 🏆 Multi-Agent "Study Streamliner": An Adaptive LLM System for Verifiable Learning

## 🌟 Competition Track: Concierge Agents

**Project Goal:** To transform unstructured learning goals into structured, verifiable educational modules, powered by specialized AI agents. The system provides real-time, accurate content and ensures accountability through a graded, interactive quiz.

---

## 💡 Problem and Value Proposition

### Problem Statement
Traditional methods of personalized study are inefficient. Human tutors are costly, and relying on general-purpose LLM chatbots often leads to unreliable, unverified, or hallucinated content without any formal mechanism for evaluation. Students lack a structured, reliable, and measurable feedback loop to confirm their learning.

### Solution and Value
The Study Streamliner solves this by leveraging a multi-agent system to guarantee **structure, accuracy, and accountability**.

* **Structure:** The Planner Agent enforces a predictable learning path (Plan → Teach → Quiz).
* **Accuracy:** The Teacher Agent uses a **real-time Google Search Tool** to ensure the content is factual and up-to-date (RAG).
* **Accountability:** The Evaluator Agent provides a measurable outcome (the score) and **personalized feedback**, ensuring the learning is verified.

**This system provides an on-demand, adaptive, and trustworthy educational experience.**

---

## ⚙️ Architecture and Agent Flow

The Streamliner operates as a **Sequential Multi-Agent System** where the output of one specialized agent is the required input for the next, ensuring a controlled and reliable workflow.

### 

### Agent Roles

| Agent | Core Responsibility | Key Technical Feature |
| :--- | :--- | :--- |
| **1. Planner Agent** (`planner_agent.py`) | **Task Decomposition.** Takes the user's goal (topic/difficulty) and creates a structured **JSON study plan**. | Enforces **Structured Output (JSON Schema)** for reliable A2A communication. |
| **2. Teacher Agent** (`teacher_agent.py`) | **Content Generation & Retrieval.** Generates the detailed lesson based on the plan. | Integrates the **Google Search Tool** (Retrieval Augmented Generation) for factual accuracy. |
| **3. Evaluator Agent** (`evaluator_agent.py`) | **Evaluation & Feedback.** Creates the quiz from the lesson content, grades the user's answers, and provides comprehensive explanations. | Provides the crucial **Measurable Outcome** and **Local Grading Logic**. |

---

## ✅ Technical Implementation Checklist

This project demonstrates the mandatory and high-value features for the Capstone competition:

* ✅ **Multi-Agent System:** Three distinct, communicating agents.
* ✅ **Tools/API Usage:** Integration of the **Google Search Tool**.
* ✅ **Structured Output:** Extensive use of **JSON Schemas** to ensure predictable data exchange between agents.
* ✅ **Robustness (Compliance Mode):** The agents contain logic to run in **Online Mode** (on the judge's platform) and seamlessly switch to **Compliance Offline Mode** for local testing without crashing.
* ✅ **Interactive Experience:** The system features a custom function for an **interactive, console-based quiz**.

---

## 🚀 Setup and Execution Instructions

### Prerequisites
1.  **Python 3.9+** installed.
2.  A terminal/command prompt (e.g., VS Code Integrated Terminal).

source venv/bin/activate