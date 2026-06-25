# AI-Powered Resume Screening & Candidate Ranking System

This project aims to develop an AI-powered system that automates the resume screening and candidate ranking process. It analyzes resumes, extracts relevant information, evaluates candidate suitability against job requirements, and generates a ranked shortlist of applicants.

## Project Structure

The project is organized into a single root directory to ensure clarity, portability, and ease of evaluation. Below is an outline of the main directories and their contents:

```
project_ai_resume_screener/
├── src/
│   ├── backend/             # Backend API and business logic (e.g., Flask/FastAPI app)
│   ├── frontend/            # Frontend application (e.g., React/Vue app for the dashboard)
│   ├── ai_models/           # AI/ML model definitions, training scripts, and inference code
│   └── utils/               # General utility functions and helper scripts
├── data/
│   ├── raw/                 # Raw input data (e.g., sample resumes, job descriptions)
│   ├── processed/           # Processed data, feature stores, or extracted information
│   └── samples/             # Sample datasets or testing data as required for deliverables
├── docs/
│   ├── README.md            # Project overview, setup instructions, and usage guide
│   ├── MODEL_DOC.md         # Documentation for AI models, methodologies, and performance
│   ├── REPORT.md            # Project report, evaluation, and future improvements
│   └── screenshots/         # Screenshots or visual assets for documentation
├── config/
│   └── settings.py          # Configuration files for the application and models
├── models/
│   └── trained_models/      # Directory to store trained AI model weights and artifacts
├── notebooks/
│   └── exploratory_analysis.ipynb # Jupyter notebooks for EDA, prototyping, and experimentation
├── tests/
│   ├── unit/                # Unit tests for individual components
│   └── integration/         # Integration tests for system modules
├── .gitignore               # Specifies intentionally untracked files to ignore
├── requirements.txt         # Python dependencies
└── Dockerfile               # Dockerfile for containerization (optional)
```

## Key Features

- **Resume Processing**: Upload, text extraction, and handling of various resume formats.
- **Candidate Information Extraction**: Extraction of key details like name, contact, skills, education, and experience.
- **Job Description Analysis**: Parsing job descriptions to identify required skills and qualifications.
- **Candidate Matching Engine**: Comparison of resumes against job descriptions, scoring, and ranking.
- **AI Features**: Skill matching, semantic similarity, resume summarization, keyword extraction, and recommendation generation.
- **Interactive Dashboard**: User interface for uploading resumes, viewing rankings, comparing candidates, and exporting results.

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Flask (for backend API)
- **NLP/ML Libraries**: PyPDF2 (for PDF text extraction), scikit-learn (for TF-IDF and cosine similarity)
- **Frontend**: Basic HTML/JavaScript for demonstration purposes

## Deliverables

- Complete Source Code
- GitHub Repository (will be provided upon completion)
- README Documentation
- Sample Dataset or Testing Data (e.g., `data/raw/job_description_sample.txt`)
- Model Documentation (`docs/MODEL_DOC.md`)
- Project Report (`docs/REPORT.md`)
- Screenshots or Demo Video (to be placed in `docs/screenshots`)

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <your-github-repo-link>
    cd project_ai_resume_screener
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install `PyPDF2` dependencies** (if not already installed by pip):
    ```bash
    pip install PyPDF2
    ```

## Usage

### Running the Backend API

1.  Navigate to the `src/backend` directory:
    ```bash
    cd src/backend
    ```
2.  Run the Flask application:
    ```bash
    python app.py
    ```
    The API will be accessible at `http://127.0.0.1:5000`.

### Using the Frontend Dashboard

Open `src/frontend/index.html` in your web browser to access the basic dashboard. Note that the frontend is a simplified demonstration and would require further development to fully interact with the backend API.

### API Endpoints

-   **`/api/process_resume` (POST)**:
    -   Uploads a PDF resume file.
    -   **Request**: `multipart/form-data` with a file named `resume`.
    -   **Response**: JSON containing extracted information and a text snippet.

-   **`/api/rank_candidates` (POST)**:
    -   Ranks candidates based on a job description and a list of resumes.
    -   **Request**: JSON with `job_description` (string) and `resumes` (list of objects with `id` and `text`).
    -   **Response**: JSON containing a ranked list of candidates with their scores.

## Contributing

Guidelines for contributing to the project will be added here.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
