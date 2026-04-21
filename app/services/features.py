skills_list = [
    "python", "machine learning", "deep learning",
    "nlp", "tensorflow", "pytorch",
    "aws", "docker", "sql", "java"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in skills_list if skill in text]


def skill_match_score(resume_skills, job_skills):
    if not job_skills:
        return 0
    return len(set(resume_skills).intersection(set(job_skills))) / len(job_skills)