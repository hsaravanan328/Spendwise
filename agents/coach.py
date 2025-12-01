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
# Coach User
# --------------------------------------------------------
def coach_user(analysis, question):
    """
    Uses Gemini to give friendly, human-like financial coaching
    based on the user's question and analysis.
    """

    prompt = f"""
You are SpendWise, a warm and friendly financial coach.

User question:
{question}

Spending analysis:
{analysis}

Write advice that is:
- Supportive and non-judgmental
- Short (2–4 sentences)
- Simple and practical
- Specific to the user's situation
- Sounds like a caring friend, NOT an AI or lecturer
- Includes one actionable next step

Tone: warm, conversational, human.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        # Fallback for Streamlit Cloud failure
        return (
            "I couldn't reach the AI model right now. But based on your spending, "
            "try to focus on one small improvement this week — maybe reducing one category "
            "or setting a simple daily limit. Small wins stack up. You've got this! 💛"
        )
