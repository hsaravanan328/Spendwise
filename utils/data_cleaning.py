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
