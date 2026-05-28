from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(
    api_key=GROQ_API_KEY
)


def generate_ai_response(prompt: str) -> str:
    """
    Centralized Groq LLM response generator
    """

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an advanced ATS resume analyzer "
                    "and recruitment intelligence AI."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1000
    )

    return response.choices[0].message.content