import streamlit as st
import sys
import os

# Add the project root to sys.path to allow imports from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.core.engine import ResumeAIEngine

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("📄 AI-Powered Resume Screening & Ranking")
st.markdown("""
This system uses **Advanced NLP (Sentence Transformers)** for semantic matching and **BART** for document summarization.
""")

@st.cache_resource
def load_engine():
    return ResumeAIEngine()

engine = load_engine()

# Sidebar for Job Description
st.sidebar.header("📋 Job Requirements")
jd_text = st.sidebar.text_area("Enter Job Description:", height=300, placeholder="Paste the job requirements here...")

# Main Area for Resume Upload
st.header("📤 Upload Resumes")
uploaded_files = st.file_uploader("Choose PDF resumes", type="pdf", accept_multiple_files=True)

if uploaded_files and jd_text:
    st.header("📊 Candidate Rankings")
    
    results = []
    
    for uploaded_file in uploaded_files:
        with st.spinner(f"Processing {uploaded_file.name}..."):
            # 1. Extract Text
            text = engine.extract_text(uploaded_file)
            
            # 2. Extract Entities
            entities = engine.extract_entities(text)
            
            # 3. Summarize
            summary = engine.summarize_resume(text)
            
            # 4. Calculate Match
            score = engine.calculate_match(text, jd_text)
            
            results.append({
                "Name": uploaded_file.name,
                "Score": round(score * 100, 2),
                "Email": entities['email'],
                "Summary": summary,
                "Full Text": text
            })
    
    # Sort by Score
    results = sorted(results, key=lambda x: x['Score'], reverse=True)
    
    # Display Results
    for i, res in enumerate(results):
        with st.expander(f"#{i+1} {res['Name']} - Match Score: {res['Score']}%"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"**Email:** {res['Email']}")
                st.metric("Match Score", f"{res['Score']}%")
            with col2:
                st.write("**AI Summary:**")
                st.info(res['Summary'])
            
            if st.checkbox(f"Show Full Text for {res['Name']}", key=res['Name']):
                st.text(res['Full Text'])

elif not jd_text:
    st.info("Please enter a Job Description in the sidebar to start ranking.")
else:
    st.info("Upload one or more resumes to begin.")
