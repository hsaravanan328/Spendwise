from agents.analyzer import analyze_spending
from agents.coach import coach_user

def run_root_agent(prompt, df):
    """
    Root agent that orchestrates the analysis and coaching.

    Parameters
    ----------
    prompt : str
        User's question
    df : pandas.DataFrame
        Transaction data

    Returns
    -------
    analysis : dict or str
        Structured analysis of the user's spending
    advice : str
        Natural-language recommendation for the user
    """
    # Run analysis (pattern matching, calculations, etc.)
    analysis = analyze_spending(prompt, df)

    # Generate advice based on analysis
    advice = coach_user(analysis, prompt)

    return analysis, advice
