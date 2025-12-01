import streamlit as st
import google.generativeai as genai
from utils.config import MODEL_NAME

# --------------------------------------------------------
# Load Gemini model ONCE (Streamlit Cloud Safe)
# --------------------------------------------------------
@st.cache_resource
def load_gemini_model():
    return genai.GenerativeModel(MODEL_NAME)

model = load_gemini_model()

# --------------------------------------------------------
# Categorize Transaction
# --------------------------------------------------------
def categorize_transaction(description, details=None):
    prompt = f"""
You are a bank transaction categorizer.

Choose ONE category from this list:
Groceries, Dining, Coffee, Shopping, Transport, Travel, Health,
Entertainment, Bills, Utilities, Education, Subscriptions,
Income, Other.

Description: {description}
Details: {details}

Return ONLY the category name with no extra text.
"""

    try:
        resp = model.generate_content(prompt)
        return resp.text.strip()

    except Exception:
        # Fail-safe → Keeps app running even if AI call breaks
        return "Other"
