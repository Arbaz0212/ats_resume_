# ATS_RESUME_ANALYZER
AI-Powered ATS Resume Screening System A production-ready Applicant Tracking System that automatically analyzes, scores, and ranks resumes against job descriptions using skill intelligence, semantic similarity, and weighted ATS logic. Built with FastAPI &amp; Streamlit to simulate real-world recruiter workflows.
🚀 AI-Powered Applicant Tracking System (ATS)

Enterprise-grade resume screening & candidate ranking platform powered by AI
Automatically analyzes, scores, ranks, and shortlists up to 1000 resumes at once against a job description with realistic ATS logic.

📌 Overview

This project is a production-ready Applicant Tracking System (ATS) designed to simulate how real-world enterprise ATS platforms (used by MNCs, consulting firms, and HR tech companies) evaluate resumes.

The system intelligently processes large-scale resume inputs, extracts only validated skills, calculates accurate ATS scores, and automatically shortlists top candidates — eliminating manual screening and reducing recruiter bias.

Unlike basic keyword-based ATS tools, this system focuses on accuracy, explainability, and scalability.

🎯 Why This ATS Is Different

Most ATS systems fail due to:

❌ Blind keyword matching

❌ Unrealistic 100% scores

❌ English phrases treated as skills

❌ Manual skill configuration per job role

❌ No transparency in rejection reasons

This system solves all of the above by design.

✨ Core Features
🔍 Intelligent Resume Screening

Upload 1 to 1000 resumes at once

Supports batch processing for enterprise hiring

Automatically ranks candidates based on ATS score

🧠 Job Description Driven Skill Matching

No hardcoded skills per role

Skills are derived directly from the job description

Uses a strict skill whitelist database to prevent noise

Eliminates false positives like:

“work closely with team”

“basic understanding of business”

“want hands-on exposure”

✅ Accurate Skill Extraction

Extracts only real, validated skills

Supports:

Programming languages

QA tools

Testing skills

Data & analytics skills

Development tools

Soft skills (controlled)

🎯 Key Capabilities

✅ Upload single or multiple resumes (up to 1000 at once)

✅ Job-description-driven skill extraction (no hardcoded skills per role)

✅ Accurate matched & missing skills detection

✅ Realistic ATS score (0–100) with float precision

✅ Section-wise scoring:

Skills

Semantic similarity

Experience

Projects

Education

✅ Automatic candidate ranking & shortlisting

✅ Recruiter-friendly Streamlit UI

✅ Production-ready FastAPI backend

📊 Realistic ATS Scoring (0–100)

Each resume receives a float-based ATS score, not a binary pass/fail.

Section-wise weighted evaluation:
Section	Weight
Skills Match	35%
JD Similarity	25%
Experience	20%
Projects	10%
Education	10%

This mirrors real hiring system logic used in enterprise recruitment.

🧮 Section Score Breakdown

For every candidate, the system provides:

Final ATS Score

Matched Skills

Missing Skills

Detailed section scores

Hire / Reject decision

📌 This makes the system fully explainable and auditable.

🏆 Automatic Shortlisting

Configurable shortlisting threshold (e.g. 80+ ATS score)

Only top candidates are shortlisted

All candidates are ranked for transparency

🖥️ Recruiter-Friendly Streamlit UI

Clean, professional interface

Upload resumes & job description

View rankings instantly

No technical knowledge required

⚙️ Scalable Backend Architecture

Built with FastAPI

Modular design

Easy to integrate with:

HR portals

Hiring dashboards

Cloud infrastructure

🧠 How the ATS Thinks (Logic Flow)

Job Description Parsing

Skill normalization using skill database

Resume skill extraction

Skill match ratio calculation

Semantic similarity analysis

Experience & project scoring

Weighted ATS score generation

Ranking & shortlisting

📂 Project Architecture
ATS_RESUME/
│
├── app/
│   ├── core/
│   │   ├── section_parser.py      # Skill extraction & matching logic
│   │   ├── similarity.py          # JD-resume similarity scoring
│   │   ├── ats_scorer.py           # Final ATS scoring logic
│   │   └── resume_parser.py        # Experience, projects, education
│   │
│   ├── models/
│   │   └── skill_db.json           # Valid skill database
│   │
│   ├── main.py                     # FastAPI entry point
│
├── streamlit_app.py                # Recruiter UI
├── requirements.txt
└── README.md

🧪 Example Output
{
  "candidate": "QA_Engineer_Resume.pdf",
  "final_score": 80.63,
  "decision": "Hire",
  "matched_skills": [
    "python",
    "sql",
    "jira",
    "manual testing",
    "regression testing"
  ],
  "missing_skills": [],
  "section_scores": {
    "skills": 100,
    "similarity": 28.22,
    "experience": 83.63,
    "projects": 80.63,
    "education": 80
  }
}

🛠️ Tech Stack

Language: Python

Backend: FastAPI

Frontend: Streamlit

NLP: Regex + semantic similarity

Architecture: Modular & scalable

🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start backend
uvicorn app.main:app --reload

3️⃣ Launch UI
streamlit run streamlit_app.py

🎓 Use Cases

Enterprise resume screening

Campus hiring automation

HR tech platforms

ATS compatibility testing

AI-powered recruitment research

📈 Future Enhancements

Role-based dynamic weighting

Resume improvement recommendations

Skill gap visualization

Cloud deployment (AWS / Azure)

Admin dashboard for recruiters

🏁 Final Note

This project demonstrates real-world ATS logic, clean backend engineering, and practical AI application in recruitment technology — making it a high-value portfolio project for roles in:

AI / ML Engineering

Backend Development

Automation Engineering

HR Tech Platforms
