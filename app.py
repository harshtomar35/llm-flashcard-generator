import streamlit as st
from utils import extract_text_from_pdf, load_model_and_tokenizer, generate_flashcards

st.set_page_config(page_title="Free Flashcard Generator", layout="wide")
st.title("🧠 Offline Flashcard Generator (No API Needed)")

model, tokenizer = load_model_and_tokenizer()

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
text_input = st.text_area("Or paste your study material here", height=300)

if st.button("Generate Flashcards"):
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
    elif text_input.strip():
        text = text_input
    else:
        st.warning("Please upload a file or paste content.")
        st.stop()

    with st.spinner("Generating..."):
        cards = generate_flashcards(text, model, tokenizer)

    if cards:
        st.success("Flashcards Generated!")
        for i, (q, a) in enumerate(cards):
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"**A{i+1}:** {a}")
            st.markdown("---")
    else:
        st.error("No flashcards created. Try with more content.")
