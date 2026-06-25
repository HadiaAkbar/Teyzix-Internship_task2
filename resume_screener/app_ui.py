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

# Custom CSS for High-End Modern Theme with Animated Background
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background: linear-gradient(135deg, #050505 0%, #0a0a12 50%, #1a1a2e 100%) !important;
        font-family: 'Poppins', 'Plus Jakarta Sans', sans-serif !important;
        color: #E2E8F0 !important;
        overflow-x: hidden;
    }
    
    /* Ensure Streamlit's main content area is transparent to show the background */
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Animated Background Elements */
    .bg-animation {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0; /* Changed from -1 to 0 to be above the gradient but below content */
        overflow: hidden;
        pointer-events: none;
    }

    /* Ensure content stays above the animation */
    [data-testid="stVerticalBlock"] {
        position: relative;
        z-index: 10;
    }

    .floating-doc {
        position: absolute;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 4px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        pointer-events: none;
        animation: float 25s infinite linear;
        opacity: 0;
    }

    /* Resume Shape */
    .resume { width: 45px; height: 60px; }
    .resume::after {
        content: '';
        position: absolute;
        top: 10px; left: 8px; right: 8px; height: 2px;
        background: rgba(255,255,255,0.15);
        box-shadow: 0 8px 0 rgba(255,255,255,0.15), 0 16px 0 rgba(255,255,255,0.15), 0 24px 0 rgba(255,255,255,0.15), 0 32px 0 rgba(255,255,255,0.15);
    }

    /* Folder Shape */
    .folder { 
        width: 55px; height: 40px; 
        border-radius: 0 6px 6px 6px;
    }
    .folder::before {
        content: '';
        position: absolute;
        top: -8px; left: 0; width: 25px; height: 8px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 6px 6px 0 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: none;
    }

    @keyframes float {
        0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.4; }
        90% { opacity: 0.4; }
        100% { transform: translateY(-20vh) translateX(20px) rotate(360deg); opacity: 0; }
    }

    /* Modern Glassmorphism Container */
    .stMarkdown, .stButton, [data-testid="stVerticalBlock"] > div {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Gradient Heading */
    .hero-heading {
        background: linear-gradient(90deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        line-height: 1.2;
        font-size: clamp(2.5rem, 6vw, 80px);
        margin-bottom: 10px;
        font-family: 'Poppins', sans-serif !important;
    }

    /* Sub-heading */
    .sub-heading {
        color: #94A3B8;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        font-size: 0.9rem;
        margin-bottom: 5px;
        font-family: 'Poppins', sans-serif !important;
    }

    /* Custom Button */
    div.stButton > button {
        background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
        width: 100%;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
        opacity: 0.95 !important;
    }

    /* Glass Cards */
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 24px !important;
        padding: 25px !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"]:hover {
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        background: rgba(255, 255, 255, 0.06) !important;
    }

    /* Input Fields */
    textarea, input, [data-testid="stFileUploadDropzone"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 16px !important;
        padding: 15px !important;
    }
    
    textarea:focus {
        border-color: #6366F1 !important;
        box-shadow: 0 0 0 1px #6366F1 !important;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 800 !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Robot Image Animation */
    @keyframes float-robot {
        0% {
            transform: translateY(0px) scale(1);
            opacity: 0.8;
        }
        50% {
            transform: translateY(-20px) scale(1.02);
            opacity: 1;
        }
        100% {
            transform: translateY(0px) scale(1);
            opacity: 0.8;
        }
    }

    .robot-container {
        animation: float-robot 4s ease-in-out infinite;
    }

    </style>

    <div class="bg-animation">
        <div class="floating-doc resume" style="left: 5%; animation-delay: 0s; animation-duration: 22s;"></div>
        <div class="floating-doc folder" style="left: 15%; animation-delay: 4s; animation-duration: 28s;"></div>
        <div class="floating-doc resume" style="left: 30%; animation-delay: 8s; animation-duration: 25s;"></div>
        <div class="floating-doc folder" style="left: 45%; animation-delay: 2s; animation-duration: 30s;"></div>
        <div class="floating-doc resume" style="left: 60%; animation-delay: 12s; animation-duration: 24s;"></div>
        <div class="floating-doc folder" style="left: 75%; animation-delay: 15s; animation-duration: 27s;"></div>
        <div class="floating-doc resume" style="left: 85%; animation-delay: 6s; animation-duration: 26s;"></div>
        <div class="floating-doc folder" style="left: 95%; animation-delay: 10s; animation-duration: 29s;"></div>
        <div class="floating-doc resume" style="left: 20%; animation-delay: 18s; animation-duration: 23s;"></div>
        <div class="floating-doc folder" style="left: 40%; animation-delay: 22s; animation-duration: 31s;"></div>
        <div class="floating-doc resume" style="left: 55%; animation-delay: 14s; animation-duration: 25s;"></div>
        <div class="floating-doc folder" style="left: 70%; animation-delay: 1s; animation-duration: 28s;"></div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown('<p class="sub-heading">AI-Powered Screening System</p>', unsafe_allow_html=True)
    col_title, col_3d = st.columns([1.8, 1.2], gap="large")
    
    with col_title:
        st.markdown('<h1 class="hero-heading">RECRUITER\'S INTELLIGENCE</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p style="font-weight: 400; color: #94A3B8; max-width: 600px; margin-bottom: 40px; font-size: 1.1rem; line-height: 1.6;">
            Elevate your hiring process with our advanced neural screening engine. 
            Designed to identify top-tier talent with surgical precision.
            </p>
        """, unsafe_allow_html=True)
    
    with col_3d:
        # Embedding the Robot model with animation
        st.markdown("""
            <div class="robot-container" style="width:100%; height:500px; background: transparent; border-radius: 30px; overflow: hidden; margin-top: -20px; display: flex; justify-content: center; align-items: center;">
                <img src="https://raw.githubusercontent.com/HadiaAkbar/Teyzix-Internship_task2/main/resume_screener/assets/robot_hero_blended.png" style="max-width: 120%; max-height: 120%; object-fit: contain;" alt="Robot as main character">
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Interaction Area
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="sub-heading">01 - CONTEXT</p>', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0;">JOB SPECIFICATIONS</h3>', unsafe_allow_html=True)
        jd_input = st.text_area(
            "Job Description",
            height=250,
            placeholder="Paste the job requirements here...",
            label_visibility="collapsed"
        )
        
        if jd_input:
            job_data = parse_job_description(jd_input)
            with st.expander("ANALYZED REQUIREMENTS"):
                st.json(job_data)

    with col2:
        st.markdown('<p class="sub-heading">02 - ASSETS</p>', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0;">CANDIDATE DOSSIERS</h3>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "Upload Resumes",
            type="pdf",
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        
        if uploaded_files:
            st.markdown(f'<p style="color: #6366F1; font-weight: 600; font-size: 0.9rem;">{len(uploaded_files)} DOCUMENTS LOADED</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Action Button
    col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])
    with col_btn_2:
        if st.button("INITIATE NEURAL SCREENING"):
            if not jd_input or not uploaded_files:
                st.warning("Please provide both job context and candidate data.")
            else:
                st.session_state['screening_triggered'] = True

    if st.session_state.get('screening_triggered'):
        process_and_display_results(jd_input, uploaded_files)

def process_and_display_results(jd_input, uploaded_files):
    st.markdown('<hr style="border: 1px solid rgba(255,255,255,0.05); margin: 40px 0;">', unsafe_allow_html=True)
    st.markdown('<h2 class="hero-heading" style="font-size: 45px; text-align: center;">SCREENING ANALYTICS</h2>', unsafe_allow_html=True)
    
    results = []
    job_data = parse_job_description(jd_input)
    
    with st.status("Analyzing candidates...", expanded=True) as status:
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
        status.update(label="Analysis complete!", state="complete", expanded=False)

    # Sort results
    ranked_results = sorted(results, key=lambda x: x['SCORE'], reverse=True)
    
    # Summary Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("CANDIDATES", len(ranked_results))
    m2.metric("TOP SCORE", f"{ranked_results[0]['SCORE']*100:.1f}%")
    m3.metric("AVG MATCH", f"{(sum(r['SCORE'] for r in ranked_results)/len(ranked_results))*100:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Detailed Cards
    for i, candidate in enumerate(ranked_results):
        score_val = candidate['SCORE'] * 100
        score_color = "#10B981" if score_val > 70 else "#F59E0B" if score_val > 40 else "#EF4444"
        
        with st.container():
            st.markdown(f"""
                <div style="background: rgba(255,255,255,0.03); padding: 25px; border-radius: 20px; border-left: 5px solid {score_color}; margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <h3 style="margin:0; color: white;">{candidate['NAME']}</h3>
                        <span style="background: {score_color}22; color: {score_color}; padding: 5px 15px; border-radius: 50px; font-weight: 700; font-size: 0.9rem;">
                            {score_val:.1f}% MATCH
                        </span>
                    </div>
                    <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">
                        <strong>AI INSIGHT:</strong> {candidate['SUMMARY']}
                    </p>
                    <p style="color: #6366F1; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
                        SKILLS: {candidate['SKILLS']}
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # Export
    df = pd.DataFrame(ranked_results)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="EXPORT DATA TO CSV",
        data=csv,
        file_name='screening_results.csv',
        mime='text/csv',
    )

if __name__ == "__main__":
    main()
