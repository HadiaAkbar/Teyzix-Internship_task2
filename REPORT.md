import PyPDF2
import re

class ResumeProcessor:
    def __init__(self):
        pass

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from a PDF file."""
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    def clean_text(self, text):
        """Cleans extracted text by removing extra whitespaces and special characters."""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\x00-\x7f]', r'', text)
        return text.strip()

    def process_resume(self, pdf_path):
        """Full resume processing pipeline."""
        raw_text = self.extract_text_from_pdf(pdf_path)
        cleaned_text = self.clean_text(raw_text)
        return cleaned_text

if __name__ == "__main__":
    # Example usage (assuming a sample resume exists)
    processor = ResumeProcessor()
    # sample_resume_path = "data/raw/sample_resume.pdf"
    # text = processor.process_resume(sample_resume_path)
    # print(text)
    print("ResumeProcessor module initialized.")
