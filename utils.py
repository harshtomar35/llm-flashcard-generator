from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import pdfplumber

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def load_model_and_tokenizer():
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    return model, tokenizer

def generate_flashcards(text, model, tokenizer):
    flashcards = []
    sentences = text.split(". ")[:15]
    
    for sentence in sentences:
        prompt = f"generate question: {sentence}"
        inputs = tokenizer.encode(prompt, return_tensors="pt", truncation=True)
        outputs = model.generate(inputs, max_length=50)
        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # For answer, use original sentence
        flashcards.append((question, sentence.strip()))
    
    return flashcards
