import streamlit as st
import requests

API_URL = "https://ats-resume-backend-i5e5.onrender.com"

st.set_page_config(
    page_title="ATS Resume Analyzer",
    layout="wide"
)

st.title("📄 ATS Resume Analyzer")
st.caption("Upload resumes and analyze ATS score against Job Description")

# ---------------------------
# Job Description input
# ---------------------------

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

# ---------------------------
# Resume upload
# ---------------------------

st.subheader("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------
# Analyze button
# ---------------------------

if st.button("🚀 Analyze Resumes"):

    if not job_role or not job_description or not uploaded_files:

        st.error(
            "Please provide Job Role, Job Description, and at least one resume."
        )

    else:

        with st.spinner("Analyzing resumes..."):

            files = [
                ("resumes", (file.name, file, "application/pdf"))
                for file in uploaded_files
            ]

            data = {
                "job_description": job_description,
                "role": job_role.lower()
            }

            try:

                response = requests.post(
                    API_URL,
                    files=files,
                    data=data
                )

                # ---------------------------------
                # BACKEND ERROR
                # ---------------------------------

                if response.status_code != 200:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

                    st.text(response.text)

                else:

                    result = response.json()

                    # ---------------------------------
                    # SAFE FALLBACKS
                    # ---------------------------------

                    shortlisted = result.get("shortlisted", [])

                    all_candidates = result.get(
                        "all_candidates_ranked",
                        []
                    )

                    # ---------------------------------
                    # SUCCESS MESSAGE
                    # ---------------------------------

                    st.success("Analysis completed successfully")

                    # ---------------------------------
                    # SUMMARY
                    # ---------------------------------

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

                    # ---------------------------------
                    # SHORTLISTED CANDIDATES
                    # ---------------------------------

                    st.subheader("✅ Shortlisted Candidates")

                    if not shortlisted:

                        st.warning("No candidates shortlisted")

                    else:

                        for c in shortlisted:

                            with st.expander(
                                f"🟢 {c.get('candidate', 'Unknown')} "
                                f"(Score: {c.get('final_score', 0)})"
                            ):

                                st.write(
                                    "**Matched Skills:**",
                                    ", ".join(
                                        c.get("matched_skills", [])
                                    )
                                )

                                st.write(
                                    "**Missing Skills:**",
                                    ", ".join(
                                        c.get("missing_skills", [])
                                    )
                                )

                                # Recommendations
                                recommendations = c.get(
                                    "recommendations",
                                    []
                                )

                                if recommendations:

                                    st.write("### Recommendations")

                                    for rec in recommendations:
                                        st.write(f"- {rec}")

                                st.json(
                                    c.get("section_scores", {})
                                )

                    # ---------------------------------
                    # ALL CANDIDATES
                    # ---------------------------------

                    st.subheader("📊 All Candidates Ranking")

                    for c in all_candidates:

                        with st.expander(
                            f"{c.get('candidate', 'Unknown')} "
                            f"— "
                            f"{c.get('decision', 'N/A')} "
                            f"({c.get('final_score', 0)})"
                        ):

                            st.write(
                                "**Matched Skills:**",
                                ", ".join(
                                    c.get("matched_skills", [])
                                )
                            )

                            st.write(
                                "**Missing Skills:**",
                                ", ".join(
                                    c.get("missing_skills", [])
                                )
                            )

                            recommendations = c.get(
                                "recommendations",
                                []
                            )

                            if recommendations:

                                st.write("### Recommendations")

                                for rec in recommendations:
                                    st.write(f"- {rec}")

                            st.json(
                                c.get("section_scores", {})
                            )

            except Exception as e:

                st.error(
                    f"Error connecting to backend: {str(e)}"
                )