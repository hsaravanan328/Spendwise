
SpendWise is a personal spending assistant that helps users analyze transactions, track budgets, categorize expenses, visualize spending, and get AI-powered financial coaching.

Built with:

*   **Streamlit**
    
*   **Google Gemini (for AI categorization + financial coaching)**
    
*   **Pandas / Plotly**
    
*   **Python**
    
*   **HuggingFace (optional sentiment model)**
    

🚀 Features
===========

### **1\. AI Transaction Categorization**

Automatically classifies transactions into categories like groceries, coffee, dining, utilities, etc.

### **2\. Budget Planner**

Set per-category monthly budgets and compare real spending vs budgets using charts.

### **3\. Spending Insights**

*   Daily spending chart
    
*   Weekday heatmap
    
*   Spending buckets (micro → major)
    
*   Severity-colored transaction table
    

### **4\. Sentiment Analysis**

Analyze transaction descriptions or user-entered text sentiment using HuggingFace or Gemini.

### **5\. Ask SpendWise**

Ask questions like:

> “Why did I spend so much this week?”“Am I overspending on food?”

AI responds with actionable, supportive financial coaching.

🗂️ Folder Structure
====================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   spendwisee/  ├── app.py  ├── pages/  │   ├── Ask_SpendWise.py  │   ├── Budget_Planner.py  │   ├── Spending_Insights.py  │   ├── Sentiment_Analysis.py  │   ├── Category_Dashboard.py  │  ├── utils/  │   ├── loader.py  │   ├── data_cleaning.py  │   ├── config.py  │   ├── categorizer.py  │   ├── analyzer.py  │   ├── coach.py  │  ├── data/  │   ├── raw_chase.csv  │   ├── cleaned.csv  │  ├── requirements.txt  └── README.md   `

🌐 Deployment (Streamlit Cloud)
===============================

### **1\. Push to GitHub**

`   git add .  git commit -m "final version"  git push   `

### **2\. Go to Streamlit Cloud → New App**

Choose your repo and set:

your GitHub repo
BranchmainApp fileapp.py

### **3\. Add your API key**

Streamlit Cloud → “Manage app” → “Secrets”

`   GOOGLE_API_KEY = "your key here"   `

Save → App auto-restarts.

### **4\. Done.**

Your app is now live!

📐 **Architecture Diagram**
===========================

Your app will be **live, stable, fast**, and **Gemini-powered**.

✅ **HOW TO DEPLOY YOUR APP ON STREAMLIT CLOUD (Step-by-Step)**
==============================================================

**Before you start**
--------------------

You must have these 4 files in your repo root:
`   requirements.txt   `

You **must NOT** commit .env.Instead, you will set your API key inside Streamlit Cloud.

🚀 **1\. Push your final project to GitHub**
============================================

In VSCode terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git add .  git commit -m "final spendwise app"  git push origin main   `

If you see “no upstream branch” error:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git push --set-upstream origin main   `

Done.

🚀 **2\. Create a Streamlit Cloud Account**
===========================================

Go to:

🔗 [https://streamlit.io/cloud](https://streamlit.io/cloud)

Login using GitHub.

🚀 **3\. Create a New App**
===========================

Click:

**New app → Pick your GitHub repo → Select branch = main → Select file = app.py**

Click **Deploy**.

🚀 **4\. Add Your API Key (MOST IMPORTANT)**
============================================

After deployment fails (or before running):

1.  Go to your deployed app
    
2.  Bottom right → **Manage app**
    
3.  Go to **Secrets**
    
4.  Paste:

`   GOOGLE_API_KEY = "your-real-key-here"   `

- ⚠️ DO NOT PUT THIS IN GITHUB
- ⚠️ DO NOT PUT .env IN REPO
- ⚠️ STREAMLIT CLOUD ONLY READS THE SECRET FROM HERE

Save → The app restarts automatically.

🚀 **5\. Add Requirements.txt**
===============================

Your requirements.txt must include:

`   streamlit  pandas  numpy  plotly  python-dotenv  google-generativeai  transformers  torch  requests  regex   `

If you don’t need HuggingFace:

❗ remove transformers + torch to make deployment faster.

==============================================================
