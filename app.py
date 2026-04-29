from transformers import pipeline
from difflib import get_close_matches

# Load better instruction-following model
chatbot = pipeline("text-generation", model="google/flan-t5-small")

# Load FAQ from file
def load_faq(file_path="faq.txt"):
    faq = {}
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if "||" in line:
            q, a = line.strip().split("||")
            faq[q.lower()] = a

    return faq

faq_data = load_faq()

# Find best matching FAQ
def get_faq_answer(user_question):
    questions = list(faq_data.keys())
    matches = get_close_matches(user_question.lower(), questions, n=1, cutoff=0.4)

    if matches:
        return faq_data[matches[0]]
    return None

# LLM response
def generate_llm_response(question):
    prompt = f"""
You are a professional customer support assistant.

Answer clearly and concisely.
If you do not know the answer, say you will escalate to human support.

Customer Question: {question}
Answer:
"""

    response = chatbot(prompt, max_new_tokens=100)[0]['generated_text']

    # Clean output
    if "Answer:" in response:
        return response.split("Answer:")[-1].strip()

    if not response.strip():
        return "I'm sorry, I couldn't understand your request. Please contact support."

    return response.strip()

# Main function (mini-agent flow)
def ask_ai(question):
    # Step 1: Try FAQ (tool)
    faq_answer = get_faq_answer(question)
    if faq_answer:
        return f"📌 FAQ Answer: {faq_answer}"

    # Step 2: Use LLM
    return f"🤖 AI Response: {generate_llm_response(question)}"