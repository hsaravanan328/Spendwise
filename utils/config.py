import streamlit as st
import google.generativeai as genai

# --------------------------------------------
# Load API key safely from Streamlit Secrets
# --------------------------------------------
API_KEY = st.secrets.get("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing GOOGLE_API_KEY in Streamlit Secrets!")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Your model
MODEL_NAME = "models/gemini-2.5-flash"
