import streamlit as st
import pandas as pd
import os
from src.utils.pdf_parser import extract_text_from_pdf
from src.data_processing.resume_parser import parse_resume
from src.data_processing.job_parser import parse_job_description
from src.matching_engine.matcher import calculate_match_score
from src.nlp_models.summarizer import summarize_text

# Page Configuration
st.set_page_config(
    page_title="AI Resume Screener | Jack",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for High-End Dark Theme (Inspired by Jack's Portfolio)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;700;900&display=swap');

    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0C0C0C !important;
        font-family: 'Kanit', sans-serif !important;
        color: #D7E2EA !important;
    }
    
    [data-testid="stHeader"] {
        background: rgba(12, 12, 12, 0.8) !important;
    }

    /* Gradient Heading */
    .hero-heading {
        background: linear-gradient(180deg, #646973 0%, #BBCCD7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -0.05em;
        line-height: 1;
        font-size: clamp(3rem, 8vw, 120px);
        margin-bottom: 20px;
    }

    /* Sub-heading */
    .sub-heading {
        color: #D7E2EA;
        font-weight: 300;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-size: clamp(0.8rem, 1.5vw, 1.2rem);
        opacity: 0.8;
    }

    /* Custom Button (Inspired by ContactButton) */
    div.stButton > button {
        background: linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 12px 40px !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        box-shadow: 0px 4px 4px rgba(181, 1, 167, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05) !important;
        opacity: 0.9 !important;
    }

    /* Cards/Containers */
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"] {
        background: #141414;
        border: 1px solid rgba(215, 226, 234, 0.1);
        border-radius: 24px;
        padding: 20px;
    }

    /* Table/Dataframe Styling */
    [data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
    }

    /* Input Fields */
    textarea, input {
        background-color: #1A1A1A !important;
        color: #D7E2EA !important;
        border: 1px solid rgba(215, 226, 234, 0.2) !important;
        border-radius: 12px !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #B600A8, #7621B0) !important;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        color: #BBCCD7 !important;
        font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown('<p class="sub-heading">AI-Powered Screening System</p>', unsafe_allow_html=True)
    col_title, col_3d = st.columns([2, 1])
    
    with col_title:
        st.markdown('<h1 class="hero-heading">HI, I\'M THE RECRUITER\'S AI</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p style="font-weight: 300; text-transform: uppercase; letter-spacing: 0.05em; color: #D7E2EA; max-width: 500px; margin-bottom: 40px;">
            An intelligent screening engine driven by crafting striking and unforgettable candidate shortlists.
            </p>
        """, unsafe_allow_html=True)
    
    with col_3d:
        # Embedding an interactive 3D model from Spline or Sketchfab for the high-end look
        st.markdown("""
            <div style="width:100%; height:300px; background: transparent; border-radius: 24px; overflow: hidden; margin-top: -40px;">
                <iframe title="Smiling Robot" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/9b1c86da128147e59bdbb9092ad40d2e/embed" width="100%" height="100%"></iframe>
            </div>
        """, unsafe_allow_html=True)

    # Main Interaction Area
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<h3 style="text-transform: uppercase; letter-spacing: 0.1em;">01 - JOB CONTEXT</h3>', unsafe_allow_html=True)
        jd_input = st.text_area(
            "Paste Job Description",
            height=300,
            placeholder="Describe the ideal candidate..."
        )
        
        if jd_input:
            job_data = parse_job_description(jd_input)
            with st.expander("VIEW EXTRACTED REQUIREMENTS"):
                st.json(job_data)

    with col2:
        st.markdown('<h3 style="text-transform: uppercase; letter-spacing: 0.1em;">02 - TALENT POOL</h3>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "Upload Resumes (PDF)",
            type="pdf",
            accept_multiple_files=True
        )
        
        if uploaded_files:
            st.markdown(f'<p style="color: #B600A8; font-weight: 500;">{len(uploaded_files)} RESUMES LOADED</p>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Action Button
    if st.button("EXECUTE SCREENING"):
        if not jd_input or not uploaded_files:
            st.warning("PLEASE PROVIDE BOTH CONTEXT AND TALENT DATA.")
        else:
            process_and_display_results(jd_input, uploaded_files)

def process_and_display_results(jd_input, uploaded_files):
    st.markdown('<h2 class="hero-heading" style="font-size: 60px;">THE RANKINGS</h2>', unsafe_allow_html=True)
    
    results = []
    job_data = parse_job_description(jd_input)
    progress_bar = st.progress(0)
    
    for idx, uploaded_file in enumerate(uploaded_files):
        # Simulation of extraction
        text = f"Simulated content from {uploaded_file.name}"
        resume_data = parse_resume(text)
        resume_data['name'] = uploaded_file.name.replace(".pdf", "").replace("_", " ").title()
        
        score = calculate_match_score(resume_data, job_data)
        summary = summarize_text(text)
        
        results.append({
            "NAME": resume_data['name'],
            "SCORE": score,
            "SUMMARY": summary,
            "SKILLS": ", ".join(resume_data.get('skills', []))
        })
        progress_bar.progress((idx + 1) / len(uploaded_files))

    # Sort results
    ranked_results = sorted(results, key=lambda x: x['SCORE'], reverse=True)
    
    # Display Summary Table
    df = pd.DataFrame(ranked_results)
    df['SCORE'] = (df['SCORE'] * 100).map('{:.1f}%'.format)
    st.dataframe(df[['NAME', 'SCORE', 'SKILLS']], use_container_width=True)

    # Detailed Cards (Sticky-stacking inspired)
    st.markdown("<br>", unsafe_allow_html=True)
    for i, candidate in enumerate(ranked_results):
        with st.container():
            c1, c2 = st.columns([1, 4])
            with c1:
                st.markdown(f'<h1 style="font-size: 80px; opacity: 0.2; margin: 0;">0{i+1}</h1>', unsafe_allow_html=True)
                st.metric("MATCH", f"{float(candidate['SCORE'].strip('%')):.1f}%")
            with c2:
                st.markdown(f'<h3 style="text-transform: uppercase; color: #BBCCD7;">{candidate["NAME"]}</h3>', unsafe_allow_html=True)
                st.write(f"**AI INSIGHT:** {candidate['SUMMARY']}")
                st.write(f"**CORE COMPETENCIES:** {candidate['SKILLS']}")
            st.markdown("---")

    # Export
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="DOWNLOAD RANKINGS DATA",
        data=csv,
        file_name='rankings.csv',
        mime='text/csv',
    )

if __name__ == "__main__":
    main()
