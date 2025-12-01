import streamlit as st
from textblob import TextBlob
from utils.loader import load_transactions
import pandas as pd

st.set_page_config(page_title="Sentiment Analysis", layout="wide")

st.title("💭 Sentiment Analysis")

# -----------------------------
# 1) Free text sentiment
# -----------------------------
st.subheader("📝 Enter text to analyze:")

text = st.text_area("Type something about your spending...",
                    height=150,
                    placeholder="Example: I feel like I’ve been overspending on coffee lately.")

def label(score: float) -> str:
    if score > 0.3:
        return "Positive 😊"
    elif score < -0.3:
        return "Negative 😞"
    return "Neutral 😐"

if st.button("Analyze Text"):
    if text.strip():
        blob = TextBlob(text)
        score = blob.sentiment.polarity
        st.success(f"**Sentiment:** {label(score)} (polarity = `{score:.3f}`)")
    else:
        st.warning("Please type something first.")

st.markdown("---")

# -----------------------------
# 2) Sentiment for transactions
# -----------------------------
st.subheader("📦 Sentiment for Transaction Descriptions")

df = load_transactions()
df["Posting Date"] = pd.to_datetime(df["Posting Date"], errors="coerce")
df = df.dropna(subset=["Posting Date"])

# compute polarity on Description
df["Sentiment Score"] = df["Description"].astype(str).apply(
    lambda t: TextBlob(t).sentiment.polarity
)
df["Sentiment Label"] = df["Sentiment Score"].apply(label)

# ---- Filters ----
col1, col2, col3 = st.columns(3)

with col1:
    start_date = st.date_input("From", df["Posting Date"].min().date())

with col2:
    end_date = st.date_input("To", df["Posting Date"].max().date())

with col3:
    limit = st.number_input("Show last N rows", min_value=5, max_value=200, value=20)

mask = (
    (df["Posting Date"].dt.date >= start_date)
    & (df["Posting Date"].dt.date <= end_date)
)
filtered = df[mask].copy()
filtered["Amount"] = filtered["Amount"].astype(float).round(2)

st.write(f"Showing last **{limit}** transactions in this period:")

st.dataframe(
    filtered[["Posting Date", "Description", "Amount", "Sentiment Label", "Sentiment Score"]]
    .sort_values("Posting Date", ascending=False)
    .head(limit),
    hide_index=True,
)
