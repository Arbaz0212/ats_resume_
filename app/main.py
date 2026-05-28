from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pdfplumber

from app.core.section_parser import extract_skills
from app.core.ats_scorer import calculate_final_ats_score

# ============================================================
# FASTAPI INIT
# ============================================================

app = FastAPI(
    title="AI Powered ATS Resume Analyzer",
    version="2.0.0"
)

# ============================================================
# CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# HOME ROUTE
# ============================================================

@app.get("/")
def home():
    return {
        "message": "ATS Resume Analyzer Running Successfully"
    }

# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(file: UploadFile) -> str:

    text = ""

    try:

        file.file.seek(0)

        with pdfplumber.open(file.file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        print(f"PDF Extraction Error: {e}")

    return text.strip()

# ============================================================
# HIRING DECISION
# ============================================================

def hiring_decision(score: float) -> str:

    if score >= 80:
        return "Hire"

    elif score >= 65:
        return "Borderline"

    else:
        return "Reject"

# ============================================================
# ANALYZE ENDPOINT
# ============================================================

@app.post("/analyze")
async def analyze_resumes(
    resumes: List[UploadFile] = File(...),
    job_description: str = Form(...),
    role: str = Form(...)
):

    results = []

    # ========================================================
    # PROCESS EACH RESUME
    # ========================================================

    for resume in resumes:

        try:

            # ------------------------------------------------
            # EXTRACT RESUME TEXT
            # ------------------------------------------------

            resume_text = extract_text_from_pdf(resume)

            if not resume_text:

                results.append({

                    "candidate": resume.filename,

                    "final_score": 0,

                    "decision": "Error",

                    "matched_skills": [],

                    "missing_skills": [],

                    "section_scores": {},

                    "error": "Unable to extract text from PDF"
                })

                continue

            # ------------------------------------------------
            # CALCULATE ATS SCORE
            # ------------------------------------------------

            ats_result = calculate_final_ats_score(
                resume_text=resume_text,
                job_description_text=job_description,
                job_role=role
            )

            final_score = ats_result.get("final_score", 0)

            # ------------------------------------------------
            # BUILD RESPONSE
            # ------------------------------------------------

            candidate_data = {

                "candidate": resume.filename,

                "final_score": round(final_score, 2),

                "decision": hiring_decision(final_score),

                "matched_skills": ats_result.get(
                    "matched_skills",
                    []
                ),

                "missing_skills": ats_result.get(
                    "missing_skills",
                    []
                ),

                "section_scores": ats_result.get(
                    "section_scores",
                    {}
                )
            }

            results.append(candidate_data)

        except Exception as e:

            print(f"Resume Processing Error: {e}")

            results.append({

                "candidate": resume.filename,

                "final_score": 0,

                "decision": "Error",

                "matched_skills": [],

                "missing_skills": [],

                "section_scores": {},

                "error": str(e)
            })

    # ========================================================
    # SORT RANKINGS
    # ========================================================

    ranked_results = sorted(
        results,
        key=lambda x: x.get("final_score", 0),
        reverse=True
    )

    # ========================================================
    # SHORTLISTED
    # ========================================================

    shortlisted = [

        r for r in ranked_results

        if r.get("final_score", 0) >= 75
    ]

    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return {

        "job_role": role,

        "total_resumes": len(resumes),

        "shortlisted": shortlisted,

        "all_candidates_ranked": ranked_results
    }