import re
from app.ai.groq_client import generate_ai_response


# ============================================================
# SAFE SCORE EXTRACTION
# ============================================================

def extract_score(response_text: str) -> float:
    """
    Extract numeric ATS similarity score from AI response.
    """

    try:
        match = re.search(r"\b(\d{1,3})\b", response_text)

        if match:
            score = float(match.group(1))

            # Clamp between 0 and 100
            return max(0.0, min(score, 100.0))

        return 50.0

    except Exception:
        return 50.0


# ============================================================
# AI SEMANTIC SIMILARITY
# ============================================================

def calculate_similarity(
    resume_text: str,
    jd_text: str
) -> float:
    """
    AI-powered semantic ATS similarity analysis using Groq.
    """

    try:

        # Prevent oversized prompts
        resume_text = resume_text[:4000]
        jd_text = jd_text[:4000]

        prompt = f"""
You are an advanced ATS (Applicant Tracking System) evaluator.

Analyze the semantic similarity between the following resume and job description.

Evaluate based on:
1. Technical skill alignment
2. Experience relevance
3. Project relevance
4. ATS keyword optimization
5. Semantic compatibility
6. Domain relevance
7. Industry fit

Return ONLY a single numeric similarity score between 0 and 100.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

        response = generate_ai_response(prompt)

        return extract_score(response)

    except Exception as e:
        print(f"[SIMILARITY ERROR]: {e}")

        # Safe fallback
        return 50.0