# Flashcard Generator using T5 (Offline, No API Required)

This is a simple Streamlit app that generates 10–15 flashcards from text or PDFs using the open-source `t5-small` model.

## 🚀 Features
- Accepts text or PDF input
- Generates question-answer flashcards
- Completely offline, no API key required
- Easy to use Streamlit interface

## 🧠 Model Used
- `t5-small` from Hugging Face Transformers
- Tokenizer: T5Tokenizer

## 💻 Setup

```bash
git clone https://github.com/harshtomar35/llm-flashcard-generator.git
cd llm-flashcard-generator
pip install -r requirements.txt
streamlit run app.py
