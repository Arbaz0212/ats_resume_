from fastapi import APIRouter, UploadFile, Form
from app.core.resume_parser import parse_resume
from app.core.ats_scorer import calculate_ats_score
from app.core.formatter_check import check_formatting
from app.ai.ollama_client import ai_suggestions
from pydantic import BaseModel
from typing import List, Dict


class SectionScores(BaseModel):
    skills: float
    experience: float
    projects: float
    education: float
    similarity: float


class ATSAnalysisResponse(BaseModel):
    role: str
    total_score: float
    section_scores: SectionScores
    matched_skills: List[str]
    missing_skills: List[str]


class FullAnalysisResponse(BaseModel):
    ats_analysis: ATSAnalysisResponse
    formatting_issues: List[str]
    ai_suggestions: str


router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile,
    job_description: str = Form(...),
    role: str = Form(...)
):
    resume_text = parse_resume(resume)

    ats_result = calculate_ats_score(
        resume_text=resume_text,
        jd_text=job_description,
        role=role
    )

    formatting_issues = check_formatting(resume_text)
    ai_feedback = ai_suggestions(resume_text, job_description)

    return {
        "ats_analysis": ats_result,
        "formatting_issues": formatting_issues,
        "ai_suggestions": ai_feedback
    }
