# AI-Powered Resume Screening & Candidate Ranking System

## Overview
The **AI-Powered Resume Screening & Candidate Ranking System** is a sophisticated and intelligent recruitment engine designed to streamline and automate the talent evaluation process. This system features a modern, dark-themed dashboard, drawing inspiration from contemporary creator portfolios, and leverages advanced Natural Language Processing (NLP) techniques to effectively bridge the gap between job requirements and candidate capabilities.

## Key Features
*   **Resume Parsing**: Automated extraction of textual and structured data, including skills, experience, and contact information, from various PDF resume formats.
*   **Job Description Analysis**: Comprehensive analysis of job descriptions to accurately identify and categorize essential skills, qualifications, and responsibilities.
*   **Intelligent Matching**: Utilizes semantic similarity algorithms and skill-based matching to quantify the compatibility between candidates and specific job roles.
*   **Candidate Ranking**: Ranks applicants based on their overall suitability and alignment with the requirements of a given position, facilitating efficient candidate selection.
*   **Summarization**: Generates concise and informative summaries of candidate profiles, highlighting key attributes and relevant experience.
*   **API Interface**: Provides a robust RESTful API, enabling seamless integration with existing HR tools and platforms.
*   **Interactive 3D Dashboard**: A high-end user interface incorporating an embedded 3D model viewer, enhancing the aesthetic and interactive experience for recruiters.

## Technology Stack
This project is built using a modern and efficient technology stack, ensuring scalability, performance, and ease of development.

| Category          | Technologies                                      |
| :---------------- | :------------------------------------------------ |
| **Backend**       | FastAPI, Uvicorn, SQLAlchemy                      |
| **NLP & ML**      | spaCy, scikit-learn, Transformers, sentence-transformers |
| **Data Handling** | PyPDF2, pandas, numpy, python-dotenv              |
| **Frontend**      | Streamlit, Altair                                 |
| **Testing**       | pytest                                            |

## Project Structure
The project adheres to a clear and modular folder structure, designed for maintainability and scalability. The core logic resides within the `resume_screener` directory.

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

## Getting Started
To set up and run the project locally, follow these steps:

### Prerequisites
Ensure you have the following installed:
*   Python 3.8+
*   pip (Python package installer)

### Installation
1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd resume_screener
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
1.  **Environment Variables**: Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
2.  **Configure Settings**: Edit the newly created `.env` file to set up necessary environment variables, such as API keys or database connection strings.

### Usage
The system offers multiple ways to interact with its functionalities:

#### Option 1: Streamlit Dashboard (Recommended)
Launch the interactive web-based dashboard for a user-friendly experience:
```bash
streamlit run app_ui.py
```

#### Option 2: API Server
Start the FastAPI server to access the system's functionalities via RESTful API endpoints:
```bash
uvicorn src.api.app:app --reload
```

#### Option 3: Command Line
Execute the core logic directly via a Python script for batch processing or specific tasks:
```bash
python src/main.py
```

## Further Documentation
For more in-depth information, please refer to the dedicated documentation files:
*   [Model Documentation](docs/MODEL_DOCS.md)
*   [API Documentation](docs/API_DOCS.md)
*   [Folder Structure Details](docs/FOLDER_STRUCTURE.md)

## Evaluation Criteria
This system has been developed with a focus on the following key evaluation criteria:
*   **AI Functionality and Accuracy**: Precision and effectiveness of the AI/NLP models.
*   **Problem-Solving Approach**: Innovativeness and efficiency in addressing the core problem of resume screening.
*   **System Design and Implementation**: Robustness, scalability, and architectural soundness of the system.
*   **Documentation and Explainability**: Clarity, completeness, and accessibility of all project documentation.
*   **Code Quality and Project Structure**: Adherence to best practices in coding, readability, and logical organization.

## License
[Specify License - e.g., MIT, Apache 2.0]
