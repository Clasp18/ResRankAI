# 🚀 ResRankAI

An **end-to-end AI-powered system** that analyzes, ranks, and explains candidate resumes against a given job description using **semantic understanding + hybrid scoring + LLM-based explainability**.

---

## 🌟 Highlights

* 📄 **Resume Parsing** — Extracts text from PDF resumes
* 🧠 **Semantic Matching** — Uses transformer embeddings for deep similarity
* ⚙️ **Hybrid Ranking** — Combines semantic + skill-based scoring
* 🤖 **Explainability Layer** — LLM explains *why* a candidate is a good fit
* ⚡ **FastAPI Backend** — Production-style API system
* 🧩 **Modular Architecture** — Clean separation of services

---

## 🧠 System Architecture

```text
Frontend (planned)
        ↓
FastAPI Backend
        ↓
---------------------------------
| Parser Service               |
| Embedding Service           |
| Ranking Engine              |
| Explainability (LLM)        |
---------------------------------
        ↓
Results (Ranked Candidates)
```

---

## 🔍 How It Works

1. 📥 Upload resumes + job description
2. 📄 Extract text from resumes
3. 🧠 Generate embeddings using transformer models
4. 📊 Compute semantic similarity
5. 🧩 Extract and match relevant skills
6. ⚖️ Compute final hybrid score
7. 🤖 Generate LLM-based explanation
8. 🏆 Return ranked candidates

---

## ⚙️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 🤗 Sentence Transformers
* 🤖 OpenAI API
* 📊 Scikit-learn

---

## 📁 Project Structure

```text
resume_ai/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── parser.py
│   │   ├── embedding.py
│   │   ├── ranking.py
│   │   ├── features.py
│   │   └── explain.py
│   ├── core/
│   │   └── config.py
│
├── data/
├── notebooks/
├── requirements.txt
└── README.md
```

---

## 📊 Example Output

```json
{
  "ranked_candidates": [
    {
      "filename": "resume_ml.pdf",
      "semantic_score": 0.78,
      "skill_score": 0.66,
      "final_score": 0.75,
      "matched_skills": ["python", "nlp"],
      "explanation": "The candidate demonstrates strong NLP and Python expertise but lacks AWS deployment experience."
    }
  ]
}
```

---

## 🚀 Getting Started

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-ai-screener.git
cd resume-ai-screener
```

---

### 🔹 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Set Environment Variables

Create `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

---

### 🔹 5. Run Server

```bash
uvicorn app.main:app --reload
```

---

### 🔹 6. Open API Docs

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoint

### 🔹 `/api/analyze`

**Input:**

* Job description (text)
* Resume files (PDF)

**Output:**

* Ranked candidates
* Scores
* Matched skills
* AI-generated explanation

---

## 🔥 Key Features Explained

### 🧠 Semantic Matching

Uses transformer embeddings to understand **context**, not just keywords.

---

### ⚙️ Hybrid Ranking

```text
Final Score = 0.7 * Semantic Score + 0.3 * Skill Match
```

---

### 🤖 Explainability

Generates human-readable reasoning:

* Why candidate fits
* Missing skills
* Overall suitability

---

## 📈 Future Improvements

* 🎨 Frontend Dashboard (React / Next.js)
* ⚡ Batch Processing & Async Tasks
* 🗄️ Vector Database (FAISS / Pinecone)
* 📊 Experience-based scoring
* 🔁 Feedback-based learning system

---

## 🧑‍💻 Author

**A S Pratham**

---

## ⭐ If You Like This Project

Give it a ⭐ and share your feedback!
