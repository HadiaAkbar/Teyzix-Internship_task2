# AI-Powered Resume Screening & Candidate Ranking System

This project is an advanced AI system designed to automate the recruitment workflow by screening resumes, extracting key information, and ranking candidates using semantic similarity.

## 🚀 Key Features

- **Semantic Matching**: Uses `Sentence-Transformers` (`all-MiniLM-L6-v2`) to calculate the semantic similarity between resumes and job descriptions, going beyond simple keyword matching.
- **AI Summarization**: Automatically generates concise summaries of resumes using the `BART` (Bidirectional and Auto-Regressive Transformers) model.
- **Unified Dashboard**: A professional Streamlit-based interface for easy interaction, evaluation, and deployment.
- **Structured Hierarchy**: Organized into a single-root directory for improved readability and portability.

## 📁 Project Structure

```
ai_resume_screening_system/
├── src/
│   ├── core/           # Advanced NLP & AI Logic (Transformers, Summarization)
│   ├── ui/             # Streamlit Dashboard Implementation
│   └── utils/          # Helper functions
├── data/               # Sample resumes and job descriptions
├── docs/               # Project documentation and reports
├── requirements.txt    # Project dependencies
├── run_app.py          # Quick launch script
└── README.md           # Project overview
```

## 🛠️ Installation & Setup

1. **Clone the Project**:
   ```bash
   cd ai_resume_screening_system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run src/ui/app.py
   ```

## 🧠 AI Methodology

### Semantic Similarity
Unlike traditional TF-IDF which relies on word frequency, this system uses **Dense Vector Embeddings**. This allows the system to understand that a "Software Engineer" resume is a good match for a "Java Developer" role even if the exact keywords differ.

### Document Summarization
We utilize the `facebook/bart-large-cnn` model to distill long resumes into a 3-4 sentence summary, allowing recruiters to quickly grasp the candidate's core profile.

## 📝 License
MIT License
