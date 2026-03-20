# Offline Customer Support Chatbot using Ollama

## 1. Introduction

This project aims to build an offline customer support chatbot for an e-commerce platform using Ollama and the Llama 3.2 (3B) model. The goal is to evaluate the feasibility of running a local large language model (LLM) for handling customer queries while ensuring data privacy and eliminating API costs. Additionally, the project compares zero-shot and one-shot prompting techniques.

---

## 2. Methodology

We created 20 e-commerce-related customer queries adapted from technical support scenarios. Two prompt templates were designed:

- Zero-shot prompting: The model was given instructions without any example.
- One-shot prompting: The model was provided with one example to guide response style.

For each query, both prompting techniques were used to generate responses. The outputs were stored in a markdown file. Each response was manually evaluated based on:

- Relevance (1-5)
- Coherence (1-5)
- Helpfulness (1-5)

---

## 3. Results & Analysis

After evaluating the responses, it was observed that:

- One-shot prompting generally produced more structured and consistent responses.
- Zero-shot responses were sometimes vague or less detailed.
- One-shot responses followed the tone and format of the provided example more effectively.

In terms of scoring:
- One-shot prompting had higher average scores in helpfulness and relevance.
- Coherence was generally good in both methods, but slightly better in one-shot.

Example:
- Query: "How do I track my order?"
  - Zero-shot: Generic response
  - One-shot: Clear steps and guidance

---

## 4. Conclusion & Limitations

The Llama 3.2 (3B) model is capable of handling basic customer support queries in an offline setup. This approach is useful for privacy-sensitive applications.

However, there are some limitations:
- The model does not have real-time access to order data.
- Responses may sometimes be incorrect (hallucination).
- Performance is slower compared to cloud-based models.

Future improvements:
- Integrating real-time database support
- Using larger models for better accuracy
- Adding multi-turn conversation capability

---