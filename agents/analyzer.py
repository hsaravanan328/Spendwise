import streamlit as st
import google.generativeai as genai
from utils.config import MODEL_NAME

# --------------------------------------------------------
# Load Gemini model ONCE (Fast + Streamlit Cloud Safe)
# --------------------------------------------------------
@st.cache_resource
def load_gemini_model():
    return genai.GenerativeModel(MODEL_NAME)

model = load_gemini_model()

# --------------------------------------------------------
# Spending Analysis
# --------------------------------------------------------
def analyze_spending(question, df):
    # Convert dataframe safely (small format)
    df_sample = df[["Posting Date", "Description", "Amount"]].tail(50)
    transactions_text = df_sample.to_string(index=False)

    prompt = f"""
You are SpendWise, a friendly financial helper.

User question:
{question}

Here are their latest transactions (safe summary):
{transactions_text}

Provide:
- A simple explanation of what's going on in their spending
- Mention any patterns, spikes, or interesting observations
- Keep it short and friendly (2–3 sentences)
- No lists, no bullet points — just a natural explanation
"""

    try:
        resp = model.generate_content(prompt)
        return resp.text.strip()

    except Exception:
        # Keep the app alive even if Gemini is unavailable
        return "I'm having trouble analyzing your transactions right now, but your recent spending looks okay overall. Try asking again in a moment!"
