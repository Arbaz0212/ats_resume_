from pydantic import BaseModel
from typing import List


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
