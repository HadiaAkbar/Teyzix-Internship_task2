# AI & NLP Model Documentation

## Overview
This document describes the AI and NLP models used in the Resume Screening & Candidate Ranking System. The system leverages a combination of rule-based systems and machine learning models to extract information, analyze text, and match candidates to job requirements.

## 1. Resume Parsing & Information Extraction
*   **Technique**: Named Entity Recognition (NER) and Pattern Matching.
*   **Tools**: spaCy, Regular Expressions.
*   **Process**:
    *   Extract raw text from PDF using `PyPDF2` or `pdfminer`.
    *   Identify entities like Name, Email, Phone Number using spaCy's NER and custom regex patterns.
    *   Extract skills by matching against a predefined ontology of technical and soft skills.

## 2. Job Description Analysis
*   **Technique**: Keyword Extraction and Semantic Analysis.
*   **Tools**: NLTK, spaCy.
*   **Process**:
    *   Tokenize and clean job description text.
    *   Extract required and preferred skills using keyword frequency and POS tagging.
    *   Identify experience requirements through pattern matching (e.g., "X+ years of experience").

## 3. Semantic Similarity & Matching Engine
*   **Technique**: Vector Embeddings and Cosine Similarity.
*   **Models**: Sentence-Transformers (e.g., `all-MiniLM-L6-v2`) or OpenAI Embeddings.
*   **Process**:
    *   Convert resume text and job descriptions into high-dimensional vector representations.
    *   Calculate the cosine similarity between the resume vector and the job description vector.
    *   Apply weights to specific sections (e.g., skills carry more weight than education).

## 4. Resume Summarization
*   **Technique**: Abstractive or Extractive Summarization.
*   **Models**: Transformer-based models like BART or T5.
*   **Process**:
    *   Feed the cleaned resume text into a pre-trained summarization model.
    *   Generate a concise paragraph highlighting the candidate's key achievements and qualifications.

## 5. Candidate Ranking
*   **Algorithm**: Weighted Scoring Model.
*   **Factors**:
    *   Semantic Similarity Score (40%)
    *   Skill Match Percentage (40%)
    *   Experience Match (20%)
*   **Output**: A final Suitability Score between 0 and 1.

## Future Improvements
*   Fine-tuning transformer models on a large corpus of resumes and job descriptions.
*   Implementing multi-job matching using vector databases like ChromaDB or FAISS.
*   Adding sentiment analysis to evaluate the "tone" of the candidate's experience.
