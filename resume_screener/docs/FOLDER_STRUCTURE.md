# Project Folder Structure

The project is organized into a single root folder `resume_screener` to ensure portability and clarity.

```
resume_screener/
├── app_ui.py               # Streamlit Dashboard UI
├── src/                    # Source code
│   ├── api/                # API endpoints and server setup
│   ├── data_processing/    # Resume and job description parsing
│   ├── database/           # Database models and CRUD operations
│   ├── matching_engine/    # Scoring and ranking logic
│   ├── nlp_models/         # AI/NLP specific modules (summarization, etc.)
│   ├── utils/              # Utility functions (PDF parsing, cleaning)
│   ├── config.py           # Configuration settings
│   └── main.py             # Entry point
├── tests/                  # Unit and integration tests
├── data/                   # Data storage
│   ├── raw/                # Original resumes and job descriptions
│   ├── processed/          # Extracted and structured data
│   └── external/           # External resources
├── docs/                   # Project documentation
├── notebooks/              # Jupyter notebooks for experimentation
├── requirements.txt        # Dependencies
├── .env.example            # Template for environment variables
├── .gitignore              # Git ignore file
└── Dockerfile              # Containerization
```
