# 🌟 LangGenius: Multi-Tool Agent

An intelligent, modular AI agent built using **LangChain**, powered by **OpenAI**, capable of performing real-time coding, data analysis, internet search, and natural language understanding — all within a unified interface.

---

## 🚀 Project Overview

**LangGenius** is a smart multi-tool AI agent designed to act as a versatile assistant. It combines the power of:

- 📊 **DataFrame analysis**  
- 🧠 **LLM reasoning & tool selection**  
- 🔍 **Web search & real-time knowledge fetching**  
- 🧮 **Python REPL execution for dynamic computation**

> 🧩 Built with LangChain’s AgentExecutor and custom tool integration to allow zero-shot task delegation and intelligent decision making.

---

## 🛠️ Features

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🔧 Tool Integration  | Dynamically uses Python REPL, Search API, CSV agent, and more                |
| 🧠 LLM Reasoning      | Uses OpenAI GPT model to determine which tool is best for a task             |
| 📂 CSV Processing     | Upload and analyze structured data using Pandas                             |
| 🌐 Web Search         | Fetch latest data using DuckDuckGo Search Tool (or similar)                 |
| ⚡ Zero-Shot Agent    | Smart routing of user queries to the right tool without fine-tuning         |

---

## 🔄 How It Works
User Input → The agent receives a natural language query.

LLM Planning → GPT-based agent selects the appropriate tool.

Tool Execution → Executes Python, runs web search, or analyzes data.

Response Generation → Combines tool output into final answer.

---

## 🧩 Requirements
Python 3.9+

LangChain

OpenAI SDK

Pandas, NumPy, Matplotlib

DuckDuckGo Search Wrapper or SerpAPI (optional)

dotenv for API key management

---
Thank You
---
