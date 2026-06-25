# src/api/routes.py

from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter()

@router.post("/upload-resumes/")
async def upload_resumes(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files], "status": "Resumes uploaded successfully"}

@router.post("/analyze-job-description/")
async def analyze_job_description(job_description: str):
    return {"job_description": job_description, "status": "Job description analyzed"}

@router.get("/rank-candidates/")
async def rank_candidates():
    return {"message": "Candidates ranked"}
