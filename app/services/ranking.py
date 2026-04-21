from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_embedding, resume_embeddings):
    scores = cosine_similarity([job_embedding], resume_embeddings)[0]
    return scores