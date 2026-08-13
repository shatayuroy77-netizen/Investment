import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="AI Investment Research Workspace",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# CUSTOM CSS
# ==============================
st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }
    .hero-box {
        padding: 40px;
        border-radius: 20px;
        background: linear-gradient(135deg, #1f2937, #111827);
        text-align: center;
        margin-bottom: 30px;
    }
    .hero-title {
        font-size: 45px;
        font-weight: 700;
        color: white;
    }
    .hero-subtitle {
        font-size: 20px;
        color: #d1d5db;
        margin-top: 15px;
    }
    .feature-card {
        padding: 25px;
        border-radius: 15px;
        background-color: #f8fafc;
        border: 1px solid #e5e7eb;
        height: 180px;
    }
    .feature-title {
        font-size: 22px;
        font-weight: 600;
    }
    .feature-text {
        font-size: 15px;
        color: #4b5563;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        color: gray;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# SESSION STATE INITIALIZATION
# ==============================
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "recent_searches" not in st.session_state:
    st.session_state.recent_searches = []

if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

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
# HERO SECTION (Updated Tone)
# ==============================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">
            AI Investment Research Workspace 📈
        </div>
        <div class="hero-subtitle">
            Your intelligent investment companion to learn, analyze business models, 
            evaluate risks, and make empowered research decisions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# WELCOME SECTION (Updated Vibe)
# ==============================
st.header("Welcome 👋")
st.write(
    """
    This platform acts as your personal **Financial Research & Educational Companion**. 
    Instead of providing blind tips, our goal is to guide you through a structured research workflow so you can build strong analytical skills:

    - Deep-Dive Company Overview
    - Core Business Model & Revenue Sources
    - Risk & Competitive Landscape Evaluation
    - Interactive Company Comparisons
    - Comprehensive Investment Research Checklist
    """
)

# ==============================
# FEATURE CARDS
# ==============================
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Core Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
        <div class="feature-title">🔎 Company Analysis</div>
        <br>
        <div class="feature-text">Research companies with AI-generated structured insights and metrics.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
        <div class="feature-title">⚖️ Compare Companies</div>
        <br>
        <div class="feature-text">Compare competitors side-by-side based on business and research factors.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
        <div class="feature-title">📚 Investment Guide</div>
        <br>
        <div class="feature-text">Learn fundamental concepts to master your financial research journey.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================
# QUICK START
# ==============================
st.divider()
st.subheader("🚀 How to Start")
st.info(
    """
    1. Head over to **Company Analysis** to search for a stock.
    2. Review AI-generated research and financial insights.
    3. Compare multiple companies using **Compare Companies**.
    4. Save your favorite reports and download local copies for offline study.
    """
)

# ==============================
# FOOTER
# ==============================
st.divider()
st.markdown(
    """
    <div class="footer">
    AI Financial Research Workspace | Built with Python + Streamlit + AI Companion Framework
    </div>
    """,
    unsafe_allow_html=True
)
