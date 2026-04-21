print("ROUTES FILE LOADED")
from fastapi import APIRouter, File, Form, UploadFile
from typing import List
from app.core.config import TOP_K
from app.services.parser import extract_text
from app.services.embedding import get_embedding
from app.services.ranking import rank_resumes
from app.services.explain import generate_explanation
from app.services.features import extract_skills, skill_match_score

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "running"}


@router.post("/upload-resumes")
async def upload_resumes(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@router.post("/parse")
async def parse_resumes(files: List[UploadFile] = File(...)):
    return {"message": "parse works"}


@router.post("/analyze")
async def analyze_resumes(
    job_description: str = Form(...),
    files: List[UploadFile] = File(..., description="upload PDF resumes")
):
    texts = []
    filenames = []

    for file in files:
        text = extract_text(file)
        texts.append(text)
        filenames.append(file.filename)

    # Semantic ranking baseline.
    job_emb = get_embedding(job_description)
    resume_embs = [get_embedding(t) for t in texts]
    scores = rank_resumes(job_emb, resume_embs)

    job_skills = extract_skills(job_description)
    results = []

    for i in range(len(filenames)):
        resume_skills = extract_skills(texts[i])
        skill_score = skill_match_score(resume_skills, job_skills)

        semantic_score = float(scores[i])
        final_score = float(0.7 * semantic_score + 0.3 * skill_score)
        matched = list(set(resume_skills).intersection(set(job_skills)))

        results.append({
            "filename": filenames[i],
            "semantic_score": semantic_score,
            "skill_score": float(skill_score),
            "final_score": final_score,
            "matched_skills": matched,
            "resume_text": texts[i]  # temporary for explanation
        })

    results.sort(key=lambda x: x["final_score"], reverse=True)
    top_results = results[:TOP_K]

    for candidate in top_results:
        explanation = generate_explanation(
            job_description,
            candidate["resume_text"],
            candidate["matched_skills"]
        )
        if explanation:
            candidate["explanation"] = explanation

        del candidate["resume_text"]

    return {
        "ranked_candidates": top_results
    }