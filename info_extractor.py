from flask import Flask, request, jsonify
from src.ai_models.resume_processor import ResumeProcessor
from src.ai_models.info_extractor import InfoExtractor
from src.ai_models.matcher import CandidateMatcher

app = Flask(__name__)
resume_processor = ResumeProcessor()
info_extractor = InfoExtractor()
matcher = CandidateMatcher()

@app.route('/api/process_resume', methods=['POST'])
def process_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file provided"}), 400
    
    resume_file = request.files['resume']
    # Save the file temporarily
    temp_path = f"data/raw/{resume_file.filename}"
    resume_file.save(temp_path)
    
    # Process the resume
    text = resume_processor.process_resume(temp_path)
    info = info_extractor.extract_info(text)
    
    return jsonify({
        "filename": resume_file.filename,
        "extracted_info": info,
        "text": text[:500] + "..." # Return a snippet for preview
    })

@app.route('/api/rank_candidates', methods=['POST'])
def rank_candidates():
    data = request.json
    job_description = data.get('job_description')
    resumes = data.get('resumes') # Expecting a list of {id, text}
    
    if not job_description or not resumes:
        return jsonify({"error": "Missing job description or resumes"}), 400
    
    rankings = matcher.rank_candidates(resumes, job_description)
    return jsonify(rankings)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
