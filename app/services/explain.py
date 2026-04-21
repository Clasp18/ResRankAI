try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from app.core.config import OPENAI_API_KEY

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client
    if OpenAI is None or not OPENAI_API_KEY:
        return None
    _client = OpenAI(api_key=OPENAI_API_KEY)
    return _client


def generate_explanation(job_description, resume_text, matched_skills):
    if not resume_text or not resume_text.strip():
        return None

    client = _get_client()
    if client is None:
        return None

    prompt = f"""
You are an AI recruiter assistant.

Job Description:
{job_description}

Candidate Resume:
{resume_text[:1500]}

Matched Skills:
{matched_skills}

Explain briefly:
1. Why this candidate is suitable
2. What is missing
3. Overall fit
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You analyze resumes."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return None
