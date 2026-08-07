import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="About - AI Investment Workspace",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# SIDEBAR NAVIGATION
# ==============================
with st.sidebar:
    st.title("📈 AI Research")
    st.write("Your AI-powered investment research assistant.")
    st.divider()
    st.markdown("### Navigation")

    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/analysis.py", label="🔎 Company Analysis")
    st.page_link("pages/compare.py", label="⚖️ Compare Companies")
    st.page_link("pages/favorites.py", label="⭐ Favorites")
    st.page_link("pages/recent.py", label="🕒 Recent Searches")
    st.page_link("pages/guide.py", label="📚 Investment Guide")
    st.page_link("pages/about.py", label="ℹ️ About")

# ==============================
# PAGE HEADER
# ==============================
st.title("ℹ️ About AI Investment Workspace")
st.write("Learn more about the technology and vision behind this intelligent financial research platform.")

st.divider()

# ==============================
# ABOUT CONTENT
# ==============================
st.subheader("🚀 Our Mission")
st.write("""
The **AI Investment Workspace** is designed to bridge the gap between complex financial data and actionable insights. 
By leveraging advanced AI models and clean data visualization, we empower everyday investors, analysts, and enthusiasts 
to perform rigorous research in a fraction of the time.
""")

st.subheader("⚖️ Research & Educational Purpose")
st.info("""
This platform is built as an educational research workspace to empower your financial learning and decision-making. 
We provide deep-dive data and AI insights so you can do your own research, rather than offering direct financial advice.
""")

st.subheader("🛠️ Technology Stack")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    * **Frontend & UI:** Streamlit
    * **Data Processing & Analysis:** Python, Pandas, NumPy
    * **Visualizations:** Native Streamlit Charts & Metrics
    """)

with col2:
    st.markdown("""
    * **Report Export:** FPDF (Secure PDF Generation)
    * **AI Integration:** Large Language Models (LLMs)
    * **Architecture:** Modular Multi-Page Structure
    """)

st.divider()

st.subheader("📬 Support & Contact")
st.info("Have questions, feedback, or feature requests? Reach out to our development team at support@aiinvestmentworkspace.com")