# 🤖 Customer Support Chatbot (Gen AI Project)

This project is an AI-powered customer support chatbot built using Hugging Face Transformers and Streamlit. It combines rule-based FAQ retrieval with LLM-based response generation to simulate real-world customer support interactions.

## 🚀 Features
- Answers customer queries using predefined FAQs
- Uses similarity matching to handle variations in questions
- Falls back to an AI model for unknown queries
- Interactive web interface using Streamlit

## 🧠 Tech Stack
- Python
- Hugging Face Transformers (FLAN-T5)
- Streamlit
- Difflib (for similarity matching)

## 📂 Project Structure
- app.py → Core chatbot logic
- streamlit_app.py → User Interface (Streamlit)
- faq.txt → FAQ dataset
- requirements.txt → Project dependencies

## ▶️ How to Run

1. Clone the repository:
git clone <your-repo-link>

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run streamlit_app.py

## 💡 Example Queries
- How can I get a refund?
- Can I cancel my order?
- Is my payment secure?
- What is artificial intelligence?

## 🎯 Learning Outcome
Built a mini AI system combining rule-based logic with LLM-based response generation, demonstrating understanding of prompt design, similarity matching, and user interaction through a web interface.
