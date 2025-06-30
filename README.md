# 🤖 Browser Agent Automation with Gemini

This project is a minimal Python script that uses the `browser_use` framework with Google's Gemini model (`gemini-2.0-flash-exp`) to automate a browser and perform tasks using natural language instructions.

---

## 🚀 What It Does

The script launches a browser, interprets your natural language task (like searching YouTube), and interacts with web pages to fulfill the task using a Large Language Model.

In this version, it searches for **MrBeast YouTube videos** automatically using an AI-powered browser agent.

---

## 🛠️ Requirements

- Python 3.10+
- [browser_use](https://pypi.org/project/browser-use/)
- [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install them using:

```bash
pip install browser_use langchain-google-genai python-dotenv
