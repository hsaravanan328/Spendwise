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
    """Load and clean the raw Chase CSV."""
    df = pd.read_csv("data/raw_chase.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Required columns
    required = ["Details", "Posting Date", "Description", "Amount", "Balance"]
    df = df[required].copy()

    # Fix dates
    df["Posting Date"] = pd.to_datetime(
        df["Posting Date"],
        errors="coerce",
        infer_datetime_format=True
    )
    df = df.dropna(subset=["Posting Date"])

    # Fix Amount & Balance
    df["Amount"] = df["Amount"].astype(str).str.replace(",", "").astype(float)
    df["Balance"] = df["Balance"].astype(str).str.replace(",", "").astype(float)

    # Clean description (remove trailing numbers)
    df["Description"] = df["Description"].astype(str).apply(
        lambda x: re.sub(r"\d+", "", x).strip()
    )

    # If category already exists AND not empty, skip AI call
    if "Category" in df.columns and df["Category"].notna().all():
        df.to_csv("data/cleaned.csv", index=False)
        return df

    # Otherwise categorize with AI
    df = ai_batch_categorize(df)

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
