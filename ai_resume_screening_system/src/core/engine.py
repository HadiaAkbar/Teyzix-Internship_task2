import PyPDF2
import re
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch

class ResumeAIEngine:
    def __init__(self):
        # Using a lightweight, fast sentence transformer for semantic similarity
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # Using a specialized summarization pipeline
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1) # -1 for CPU

    def extract_text(self, pdf_file):
        """Extracts text from an uploaded PDF file."""
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error extracting text: {str(e)}"

    def summarize_resume(self, text):
        """Generates a concise summary of the resume."""
        if not text or len(text) < 100:
            return "Text too short to summarize."
        
        # Truncate text to fit model limits (usually 1024 tokens)
        truncated_text = text[:1000] 
        summary = self.summarizer(truncated_text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def calculate_match(self, resume_text, job_description):
        """Calculates semantic similarity between resume and JD."""
        # Compute embeddings
        embeddings = self.model.encode([resume_text, job_description])
        # Compute cosine similarity
        score = util.cos_sim(embeddings[0], embeddings[1])
        return float(score)

    def extract_entities(self, text):
        """Basic extraction for demonstration (can be expanded with NER)."""
        email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        phone = re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4})', text)
        
        return {
            "email": email.group(0) if email else "Not found",
            "phone": phone.group(0) if phone else "Not found"
        }
