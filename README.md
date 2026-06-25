AI-Powered Resume Screening & Candidate Ranking System


Link
https://teyzix-internshiptask2-e3uklr9d59hgbqnpld6uak.streamlit.app/


Overview

The AI-Powered Resume Screening & Candidate Ranking System is a high-end, intelligent recruitment engine designed to automate the evaluation of talent. Featuring a sophisticated dark-themed dashboard inspired by modern creator portfolios, it leverages advanced NLP to bridge the gap between job requirements and candidate potential.

Features

•
Resume Parsing: Automatically extracts text and structured data (skills, experience, contact info) from PDF resumes.

•
Job Description Analysis: Analyzes job descriptions to identify required skills and qualifications.

•
Intelligent Matching: Calculates semantic similarity and skill-based matching scores between candidates and jobs.

•
Candidate Ranking: Ranks applicants based on their suitability for specific roles.

•
Summarization: Generates concise summaries of candidate profiles.

•
API Interface: Provides a RESTful API for easy integration with other tools.

•
Interactive 3D Dashboard: A sophisticated UI featuring an embedded 3D model viewer for a high-end creator aesthetic.

Getting Started

Prerequisites

•
Python 3.8+

•
pip

Installation

1.
Clone the repository:

Bash


git clone <repository_url>
cd resume_screener





2.
Install dependencies:

Bash


pip install -r requirements.txt





Configuration

1.
Copy .env.example to .env.

2.
Configure your environment variables (e.g., API keys, database URLs) in the .env file.

Usage

Option 1: Streamlit Dashboard (Recommended)

Run the interactive dashboard:

Bash


streamlit run app_ui.py



Option 2: API Server

Start the FastAPI server:

Bash


uvicorn src.api.app:app --reload



Option 3: Command Line

Run the core logic via script:

Bash


python src/main.py



Project Structure

Refer to docs/FOLDER_STRUCTURE.md for a detailed breakdown of the project directory.

Documentation

•
Model Documentation

•
API Documentation

Evaluation Criteria

The system is designed to meet the following criteria:

•
AI Functionality and Accuracy

•
Problem-Solving Approach

•
System Design and Implementation

•
Documentation and Explainability

•
Code Quality and Project Structure

License

[Specify License]

