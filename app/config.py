import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# GROQ CONFIGURATION
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama-3.3-70b-versatile"

# Optional fallback model
GROQ_FALLBACK_MODEL = "llama3-70b-8192"