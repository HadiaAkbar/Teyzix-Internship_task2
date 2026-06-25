# API Documentation: Resume Screener

The Resume Screener API provides endpoints for uploading resumes, analyzing job descriptions, and retrieving candidate rankings.

## Base URL
`http://localhost:8000`

## Endpoints

### 1. Upload Resumes
*   **URL**: `/upload-resumes/`
*   **Method**: `POST`
*   **Content-Type**: `multipart/form-data`
*   **Request Body**:
    *   `files`: List of PDF files.
*   **Response**:
    ```json
    {
      "filenames": ["resume1.pdf", "resume2.pdf"],
      "status": "Resumes uploaded successfully"
    }
    ```

### 2. Analyze Job Description
*   **URL**: `/analyze-job-description/`
*   **Method**: `POST`
*   **Content-Type**: `application/json`
*   **Request Body**:
    ```json
    {
      "job_description": "We are looking for a Python developer with experience in NLP and machine learning..."
    }
    ```
*   **Response**:
    ```json
    {
      "job_description": "...",
      "status": "Job description analyzed"
    }
    ```

### 3. Rank Candidates
*   **URL**: `/rank-candidates/`
*   **Method**: `GET`
*   **Response**:
    ```json
    {
      "rankings": [
        {
          "name": "John Doe",
          "score": 0.92,
          "summary": "Experienced Python developer with strong NLP background."
        },
        {
          "name": "Jane Smith",
          "score": 0.85,
          "summary": "Machine learning engineer with focus on computer vision."
        }
      ]
    }
    ```

## Error Handling
The API uses standard HTTP status codes:
*   `200 OK`: Request successful.
*   `400 Bad Request`: Invalid input.
*   `500 Internal Server Error`: Server-side error.
