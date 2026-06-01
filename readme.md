# 🚀 ATS Resume Analyzer

> An AI-powered Applicant Tracking System (ATS) that automatically analyzes, scores, ranks, and shortlists resumes against job descriptions using intelligent skill matching, semantic similarity, and weighted ATS scoring.

Built with **FastAPI** and **Streamlit**, this project simulates real-world enterprise ATS workflows used by recruiters and HR technology platforms.

---

## 📖 Overview

Recruiters often spend hours manually reviewing hundreds of resumes for a single role.

This project automates that process by evaluating resumes against a job description and generating realistic ATS scores based on multiple hiring factors.

The system can process and rank up to **1000 resumes simultaneously**, helping recruiters identify the most relevant candidates in seconds.

Unlike traditional ATS systems that rely purely on keyword matching, this platform combines:

- Skill Intelligence
- Semantic Similarity Analysis
- Experience Evaluation
- Project Assessment
- Education Scoring

to generate transparent and explainable candidate rankings.

---

## 🎯 Problem Statement

Traditional ATS solutions suffer from several limitations:

- Blind keyword matching
- Inflated ATS scores
- Poor explainability
- False skill extraction
- Role-specific hardcoding
- Limited scalability

These issues often result in qualified candidates being incorrectly rejected or poorly ranked.

---

## 💡 Solution

This ATS uses a structured evaluation pipeline that:

1. Parses the job description.
2. Extracts validated skills.
3. Processes resumes.
4. Calculates semantic similarity.
5. Evaluates experience and projects.
6. Generates weighted ATS scores.
7. Ranks and shortlists candidates automatically.

This provides a more realistic simulation of modern recruitment workflows.

---

# ✨ Key Features

### Resume Screening

- Upload single or multiple resumes
- Supports bulk processing
- Analyze up to 1000 resumes
- Automatic candidate ranking

### Intelligent Skill Matching

- Job-description-driven skill extraction
- No hardcoded role-specific skills
- Validated skill database
- Accurate matched and missing skills detection

### ATS Scoring Engine

- Realistic ATS scores (0–100)
- Weighted evaluation system
- Section-wise scoring
- Explainable hiring decisions

### Candidate Ranking

- Automatic ranking
- Configurable shortlisting thresholds
- Transparent scoring logic

### Recruiter Dashboard

- Interactive Streamlit interface
- Resume upload portal
- Ranking visualization
- Candidate evaluation reports

---

# 🏗️ System Architecture

```text
                         Job Description
                                │
                                ▼
                    Skill Extraction Engine
                                │
                                ▼
                         Skill Database
                                │
                                ▼
                     Resume Processing Layer
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
   Skill Matching      Similarity Analysis   Resume Parsing
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                      ATS Scoring Engine
                                │
                                ▼
                      Candidate Ranking
                                │
                                ▼
                       Shortlisting System
                                │
                                ▼
                         Streamlit UI
```

---

# 🧠 ATS Evaluation Logic

Each resume is evaluated across multiple dimensions.

## Skills Match (35%)

Measures how many required job skills are present within the resume.

---

## Semantic Similarity (25%)

Calculates contextual similarity between:

```text
Job Description
        vs
Resume Content
```

This prevents candidates from gaming the system through keyword stuffing.

---

## Experience Score (20%)

Evaluates:

- Years of experience
- Relevance of experience
- Industry alignment

---

## Project Score (10%)

Measures:

- Technical depth
- Project relevance
- Demonstrated skills

---

## Education Score (10%)

Evaluates:

- Degree relevance
- Academic qualifications
- Educational alignment

---

# 📊 ATS Score Formula

```text
Final Score =
(0.35 × Skills Score)
+ (0.25 × Similarity Score)
+ (0.20 × Experience Score)
+ (0.10 × Project Score)
+ (0.10 × Education Score)
```

This produces realistic ATS scores ranging from:

```text
0 → 100
```

---

# 📂 Project Structure

```text
ATS_RESUME_ANALYZER/
│
├── app/
│   │
│   ├── core/
│   │   ├── ats_scorer.py
│   │   ├── similarity.py
│   │   ├── resume_parser.py
│   │   └── section_parser.py
│   │
│   ├── models/
│   │   └── skill_db.json
│   │
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- Python

## Frontend

- Streamlit

## NLP & AI

- Semantic Similarity Analysis
- Skill Extraction Engine
- ATS Scoring Algorithm

## Data Processing

- Regex
- Text Parsing
- Skill Normalization

---

# 🔄 Workflow

```text
Job Description
        │
        ▼
Skill Extraction
        │
        ▼
Resume Parsing
        │
        ▼
Skill Matching
        │
        ▼
Semantic Similarity
        │
        ▼
Section-wise Scoring
        │
        ▼
Final ATS Score
        │
        ▼
Candidate Ranking
        │
        ▼
Shortlisting
```

---

# 🧪 Sample Output

```json
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
```

---

# 🎯 Business Impact

This project demonstrates practical applications of:

- AI-powered recruitment automation
- Resume intelligence systems
- Semantic search
- Candidate ranking algorithms
- Explainable AI workflows
- Enterprise ATS design

---

# 🚀 Installation

## Clone Repository

```bash
git clone <repository-url>
cd ATS_RESUME_ANALYZER
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

---

## Launch Streamlit UI

```bash
streamlit run streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

---

# 🎓 Use Cases

- Enterprise Hiring
- Campus Recruitment
- HR Tech Platforms
- Resume Screening Automation
- Candidate Ranking Systems
- ATS Compatibility Analysis

---

# 📈 Future Enhancements

- Resume Improvement Suggestions
- Skill Gap Analysis
- Recruiter Analytics Dashboard
- Role-Specific Dynamic Weighting
- Cloud Deployment
- Multi-Language Resume Support
- LLM-Based Candidate Insights

---

# 👨‍💻 Author

**Arbaz**

AI Engineer | Backend Developer | Generative AI Enthusiast

GitHub: https://github.com/Arbaz0212

---

# ⭐ If you found this project useful, consider giving it a star.
