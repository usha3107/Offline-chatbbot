import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def query_ollama(prompt):
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."


# Load prompt templates
with open("prompts/zero_shot_template.txt", "r", encoding="utf-8") as f:
    zero_template = f.read()

with open("prompts/one_shot_template.txt", "r", encoding="utf-8") as f:
    one_template = f.read()

# 20 e-commerce queries (as required)
queries = [
    "My discount code is not working at checkout.",
    "How can I track my order status?",
    "I want to return an item I purchased.",
    "My payment failed but money was deducted.",
    "Can I change my delivery address after ordering?",
    "I received a damaged product.",
    "How long does shipping take?",
    "I want to cancel my order.",
    "Where can I see my past orders?",
    "I forgot my account password.",
    "Why is my order delayed?",
    "Can I exchange a product?",
    "My order shows delivered but I didn't receive it.",
    "How do I apply a coupon code?",
    "Do you offer cash on delivery?",
    "How can I contact customer support?",
    "Are there any shipping charges?",
    "I entered the wrong size, can I change it?",
    "When will I get my refund?",
    "My account is locked.",
]

# Open results file
with open("eval/results.md", "w", encoding="utf-8") as file:

    # Table header
    file.write(
        "|Query #|Customer Query|Prompting Method|Response|Relevance|Coherence|Helpfulness|\n"
    )
    file.write("|---|---|---|---|---|---|---|\n")

    # Loop through queries
    for i, query in enumerate(queries, 1):
        print(f"\n🔹 Processing Query {i}: {query}")

        # Zero-shot
        zero_prompt = zero_template.replace("{query}", query)
        zero_response = query_ollama(zero_prompt)
        print("✅ Zero-shot done")

        file.write(f"|{i}|{query}|Zero-Shot|{zero_response}| | | |\n")

        # One-shot
        one_prompt = one_template.replace("{query}", query)
        one_response = query_ollama(one_prompt)
        print("✅ One-shot done")

        file.write(f"|{i}|{query}|One-Shot|{one_response}| | | |\n")

print("\n🎉 Results saved in eval/results.md")
