from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Flask app
app = Flask(__name__)
CORS(app)

# ✅ Get OpenAI key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ Fallback if key not found
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not set in .env or environment variables.")

# ✅ Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# ✅ Load and clean dataset
filepath = "Training_Dataset.csv"
df = pd.read_csv(filepath)
df_cleaned = df.dropna(subset=["Loan_ID", "Gender", "Married", "Education", "Loan_Status"])

def row_to_text(row):
    return (
        f"Loan ID {row['Loan_ID']}: {row['Gender']}, {row['Married']} Married, "
        f"{row['Dependents']} Dependents, Education: {row['Education']}, "
        f"{'Self-Employed' if row['Self_Employed'] == 'Yes' else 'Not Self-Employed'}, "
        f"Income: {row['ApplicantIncome']}, Co-applicant Income: {row['CoapplicantIncome']}, "
        f"Loan Amount: {row['LoanAmount']}, Term: {row['Loan_Amount_Term']}, "
        f"Credit History: {row['Credit_History']}, Property: {row['Property_Area']}, "
        f"Loan Status: {row['Loan_Status']}"
    )

# ✅ Convert each row to a string chunk
text_chunks = df_cleaned.apply(row_to_text, axis=1).tolist()

# ✅ Embed all rows
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(text_chunks, show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# ✅ API endpoint
@app.route("/query", methods=["POST"])
def query_answer():
    data = request.json
    query = data.get("query", "")

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), 3)
    context = "\n".join([text_chunks[i] for i in I[0]])

    prompt = f"""
    Answer the question based on the following loan applications data:
    {context}

    Question: {query}
    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content.strip()
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
