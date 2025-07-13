import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5000/query", { query });
      setResponse(res.data.answer);
    } catch (error) {
      setResponse("Error: Could not get response. Please check if the backend server is running.");
    }
    setLoading(false);
  };

  return (
    <div className="card fade-in">
      <div style={{ textAlign: 'center', marginBottom: 'var(--spacing-8)' }}>
        <h1 style={{ marginBottom: 'var(--spacing-2)' }}>
          🔍 RAG Q&A Chatbot
        </h1>
        <p style={{ 
          color: 'var(--gray-600)', 
          fontSize: 'var(--font-size-lg)',
          marginBottom: 'var(--spacing-6)'
        }}>
          Ask questions about your loan data and get intelligent answers
        </p>
      </div>

      <form onSubmit={handleSubmit} style={{ marginBottom: 'var(--spacing-8)' }}>
        <div style={{ marginBottom: 'var(--spacing-4)' }}>
          <input
            type="text"
            placeholder="Ask a question about the loan data..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={loading}
            style={{
              marginBottom: 'var(--spacing-4)',
              fontSize: 'var(--font-size-lg)',
              padding: 'var(--spacing-5)'
            }}
          />
          <button
            type="submit"
            disabled={loading || !query.trim()}
            style={{
              width: '100%',
              background: loading 
                ? 'var(--gray-400)' 
                : 'linear-gradient(135deg, var(--primary), var(--primary-dark))',
              color: 'white',
              fontSize: 'var(--font-size-lg)',
              padding: 'var(--spacing-4)',
              opacity: (!query.trim() || loading) ? 0.6 : 1,
              cursor: (!query.trim() || loading) ? 'not-allowed' : 'pointer'
            }}
          >
            {loading ? (
              <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 'var(--spacing-2)' }}>
                <div className="pulse" style={{ 
                  width: '16px', 
                  height: '16px', 
                  borderRadius: '50%', 
                  background: 'currentColor' 
                }}></div>
                Thinking...
              </span>
            ) : (
              'Ask Question'
            )}
          </button>
        </div>
      </form>

      {response && (
        <div style={{
          background: 'var(--gray-50)',
          borderRadius: 'var(--radius-xl)',
          padding: 'var(--spacing-6)',
          border: '1px solid var(--gray-200)',
          animation: 'fadeIn 0.6s ease-out'
        }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: 'var(--spacing-2)',
            marginBottom: 'var(--spacing-4)',
            color: 'var(--gray-700)',
            fontWeight: '600'
          }}>
            <span style={{ fontSize: 'var(--font-size-xl)' }}>💡</span>
            <span>Answer</span>
          </div>
          <div style={{
            color: 'var(--gray-800)',
            lineHeight: '1.7',
            fontSize: 'var(--font-size-base)',
            whiteSpace: 'pre-wrap'
          }}>
            {response}
          </div>
        </div>
      )}

      {!response && !loading && (
        <div style={{
          textAlign: 'center',
          padding: 'var(--spacing-8)',
          color: 'var(--gray-500)',
          fontSize: 'var(--font-size-lg)'
        }}>
          <div style={{ fontSize: 'var(--font-size-4xl)', marginBottom: 'var(--spacing-4)' }}>
            🤖
          </div>
          <p>Ready to help! Ask your first question above.</p>
        </div>
      )}
    </div>
  );
}

export default App;
