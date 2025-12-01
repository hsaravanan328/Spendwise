import streamlit as st
from utils.loader import load_transactions
from agents.root import run_root_agent

# Optional: you can set layout here if not already done in app.py
# st.set_page_config(page_title="Ask SpendWise", layout="wide")

st.title("💬 Ask SpendWise")

st.caption(
    "Ask natural questions about your spending – "
    "SpendWise will analyze your recent transactions and give simple, friendly advice."
)

# Load transactions once
df = load_transactions()

# Chat history in session
if "ask_history" not in st.session_state:
    st.session_state.ask_history = []

# Chat input
question = st.chat_input("Ask something about your spending…")

if question:
    # Add user message
    st.session_state.ask_history.append(("user", question))

    with st.spinner("Thinking..."):
        try:
            analysis, advice = run_root_agent(question, df)
        except Exception as e:
            # Never expose raw error; just show friendly message
            analysis = ""
            advice = (
                "Hmm, I ran into a technical issue while analyzing your spending. "
                "Please try again in a moment. If this keeps happening, the AI quota "
                "might be temporarily exhausted."
            )

    # You can choose to keep only advice, but it’s nice to store both
    reply_text = advice
    if analysis:
        reply_text = f"**Quick check:** {analysis}\n\n**My advice:** {advice}"

    st.session_state.ask_history.append(("assistant", reply_text))

# Display chat history
for role, content in st.session_state.ask_history:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(content)
