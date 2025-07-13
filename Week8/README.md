
# 🧠 RAG Q&A Chatbot (CSV Knowledge Base)

A Retrieval-Augmented Generation chatbot using document-based context from a CSV loan dataset.

## 🔧 Tech Stack
- React (frontend)
- Flask + FAISS + SentenceTransformers + OpenAI (backend)

## 🚀 Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 💡 Ask questions like:
- "What is the income of the applicant from an urban area?"
- "Who got loan approval with a credit history of 1?"

---

Set your OpenAI API key in `app.py` to enable generation.
