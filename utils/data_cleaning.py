import pandas as pd
import re
import json
import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st

# ----------------------------------------------------
# CLEAN RAW CHASE CSV
# ----------------------------------------------------
@st.cache_data(show_spinner=False)
def clean_data():
    df = pd.read_csv("data/raw_chase.csv")

    # fix hidden spaces
    df.columns = df.columns.str.strip()

    required = ["Details", "Posting Date", "Description", "Amount", "Balance"]
    df = df[required].copy()

    # fix date
    df["Posting Date"] = pd.to_datetime(df["Posting Date"], errors="coerce")
    df = df.dropna(subset=["Posting Date"])

    # clean amount
    df["Amount"] = df["Amount"].astype(str).str.replace(",", "", regex=False).astype(float)

    # clean description
    df["Description"] = df["Description"].astype(str)

    # 🚨 if cleaned.csv exists → skip AI and load it
    import os
    if os.path.exists("data/cleaned.csv"):
        return pd.read_csv("data/cleaned.csv")

    # Otherwise just save without category
    df["Category"] = "Other"
    df.to_csv("data/cleaned.csv", index=False)
    return df


# ----------------------------------------------------
# AI BATCH CATEGORIZATION
# ----------------------------------------------------
def ai_batch_categorize(df):
    """Use Gemini to batch-categorize descriptions into known categories."""
    model = genai.GenerativeModel(MODEL_NAME)

    descriptions = df["Description"].tolist()

    prompt = f"""
Return a JSON array where each item is the category for the matching transaction.

Valid categories:
["Groceries","Dining","Coffee","Shopping","Transport","Travel","Health",
"Entertainment","Bills","Utilities","Education","Subscriptions","Income","Other"]

Descriptions:
{descriptions}

Respond ONLY with JSON. No explanation.
"""

    resp = model.generate_content(prompt)
    raw = resp.text.strip()

    # -------- Clean the AI output --------
    raw = raw.replace("```json", "")
    raw = raw.replace("```", "")
    raw = raw.strip()

    try:
        categories = json.loads(raw)
    except Exception:
        raise ValueError(
            f"❌ Gemini returned invalid JSON:\n\n{raw}"
        )

    if len(categories) != len(df):
        raise ValueError(
            f"❌ AI returned {len(categories)} categories for {len(df)} rows.\n"
            f"Output:\n{categories}"
        )

    df["Category"] = categories
    return df
