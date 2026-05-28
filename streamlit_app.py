import streamlit as st
import requests

# ============================================================
# BACKEND API
# ============================================================

API_URL = "https://ats-resume-backend-i5e5.onrender.com/analyze"

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ATS Resume Analyzer",
    layout="wide"
)

st.title("📄 ATS Resume Analyzer")

st.caption(
    "Upload resumes and analyze ATS score against Job Description"
)

# ============================================================
# JOB DESCRIPTION
# ============================================================

st.subheader("Job Description")

job_role = st.text_input(
    "Job Role",
    placeholder="QA Engineer / Data Analyst / Software Engineer"
)

job_description = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Paste the complete job description here..."
)

# ============================================================
# RESUME UPLOAD
# ============================================================

st.subheader("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button("🚀 Analyze Resumes"):

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not job_role:

        st.error("Please enter Job Role")

    elif not job_description:

        st.error("Please enter Job Description")

    elif not uploaded_files:

        st.error("Please upload at least one resume")

    else:

        with st.spinner("Analyzing resumes..."):

            try:

                # ------------------------------------------------
                # PREPARE FILES
                # ------------------------------------------------

                files = []

                for file in uploaded_files:

                    files.append(
                        (
                            "resumes",
                            (
                                file.name,
                                file,
                                "application/pdf"
                            )
                        )
                    )

                # ------------------------------------------------
                # FORM DATA
                # ------------------------------------------------

                data = {
                    "job_description": job_description,
                    "role": job_role.lower()
                }

                # ------------------------------------------------
                # API CALL
                # ------------------------------------------------

                response = requests.post(
                    API_URL,
                    files=files,
                    data=data,
                    timeout=120
                )

                # ------------------------------------------------
                # HANDLE ERRORS
                # ------------------------------------------------

                if response.status_code != 200:

                    st.error(
                        f"Backend Error: {response.status_code}"
                    )

                    st.text(response.text)

                else:

                    result = response.json()

                    shortlisted = result.get(
                        "shortlisted",
                        []
                    )

                    all_candidates = result.get(
                        "all_candidates_ranked",
                        []
                    )

                    # --------------------------------------------
                    # SUCCESS
                    # --------------------------------------------

                    st.success(
                        "Analysis completed successfully"
                    )

                    # --------------------------------------------
                    # METRICS
                    # --------------------------------------------

                    col1, col2, col3 = st.columns(3)

                    col1.metric(
                        "Job Role",
                        result.get("job_role", "N/A")
                    )

                    col2.metric(
                        "Total Resumes",
                        result.get("total_resumes", 0)
                    )

                    col3.metric(
                        "Shortlisted",
                        len(shortlisted)
                    )

                    # --------------------------------------------
                    # SHORTLISTED
                    # --------------------------------------------

                    st.subheader(
                        "✅ Shortlisted Candidates"
                    )

                    if not shortlisted:

                        st.warning(
                            "No candidates shortlisted"
                        )

                    else:

                        for candidate in shortlisted:

                            with st.expander(
                                f"🟢 {candidate.get('candidate', 'Unknown')} "
                                f"(Score: {candidate.get('final_score', 0)})"
                            ):

                                st.write(
                                    "**Decision:**",
                                    candidate.get(
                                        "decision",
                                        "N/A"
                                    )
                                )

                                st.write(
                                    "**Matched Skills:**",
                                    ", ".join(
                                        candidate.get(
                                            "matched_skills",
                                            []
                                        )
                                    )
                                )

                                st.write(
                                    "**Missing Skills:**",
                                    ", ".join(
                                        candidate.get(
                                            "missing_skills",
                                            []
                                        )
                                    )
                                )

                                st.write(
                                    "### Section Scores"
                                )

                                st.json(
                                    candidate.get(
                                        "section_scores",
                                        {}
                                    )
                                )

                    # --------------------------------------------
                    # ALL CANDIDATES
                    # --------------------------------------------

                    st.subheader(
                        "📊 All Candidates Ranking"
                    )

                    for candidate in all_candidates:

                        with st.expander(
                            f"{candidate.get('candidate', 'Unknown')} "
                            f"— "
                            f"{candidate.get('decision', 'N/A')} "
                            f"(Score: {candidate.get('final_score', 0)})"
                        ):

                            st.write(
                                "**Matched Skills:**",
                                ", ".join(
                                    candidate.get(
                                        "matched_skills",
                                        []
                                    )
                                )
                            )

                            st.write(
                                "**Missing Skills:**",
                                ", ".join(
                                    candidate.get(
                                        "missing_skills",
                                        []
                                    )
                                )
                            )

                            st.write(
                                "### Section Scores"
                            )

                            st.json(
                                candidate.get(
                                    "section_scores",
                                    {}
                                )
                            )

            except Exception as e:

                st.error(
                    f"Error connecting to backend: {str(e)}"
                )