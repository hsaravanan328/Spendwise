import streamlit as st
import pandas as pd
import plotly.express as px
from utils.loader import load_transactions

st.set_page_config(page_title="Category Dashboard", layout="wide")
st.title("📊 Category Dashboard")

# -------------------------
# Load & Clean Data
# -------------------------
df = load_transactions()

df["Posting Date"] = pd.to_datetime(df["Posting Date"], errors="coerce")
df = df.dropna(subset=["Posting Date"])

# Convert expenses to positive, income to 0
df["CleanAmount"] = df["Amount"].apply(lambda x: abs(x) if x < 0 else 0)

# -------------------------
# Category Selection
# -------------------------
categories = sorted(df["Category"].dropna().unique())

cat = st.selectbox("Choose a category:", categories)

filtered = df[df["Category"] == cat]

if filtered.empty:
    st.warning(f"No transactions found for category: {cat}")
    st.stop()

# -------------------------
# Total Spending
# -------------------------
total_spent = filtered["CleanAmount"].sum()

st.write(f"### Total Spending in **{cat}**: **${total_spent:,.2f}**")

# -------------------------
# Spending Over Time Chart
# -------------------------
fig = px.bar(
    filtered,
    x="Posting Date",
    y="CleanAmount",
    title=f"{cat} Spending Over Time",
    labels={"CleanAmount": "Amount ($)"},
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Amount ($)",
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Recent Transactions Table
# -------------------------
st.markdown("### 📄 Recent Transactions")

num_rows = st.selectbox("Show last:", [5, 10, 20, 50], index=0)

display_df = filtered[
    ["Posting Date", "Description", "Amount", "Balance", "Category"]
].sort_values("Posting Date", ascending=False)

st.dataframe(display_df.head(num_rows), hide_index=True)
