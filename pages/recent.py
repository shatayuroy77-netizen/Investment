import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Recent Searches - AI Investment Workspace",
    page_icon="🕒",
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
st.title("🕒 Recent Research History")
st.write("View and re-visit the companies and reports you have recently searched for.")

st.divider()

# ==============================
# RECENT SEARCHES STATE MANAGEMENT
# ==============================
if "recent_searches" not in st.session_state:
    st.session_state.recent_searches = []

# Optional: If other pages push to session state, we capture them
# For example, when a user searches a ticker in analysis.py, it can be appended here.

recent_searches = st.session_state.recent_searches

if recent_searches:
    st.success(f"Showing your last {len(recent_searches)} search activities.")
    
    # Display clear history button
    if st.button("🗑️ Clear Search History"):
        st.session_state.recent_searches = []
        st.rerun()

    st.divider()

    for item in recent_searches:
        with st.container(border=True):
            cols = st.columns([3, 2, 2])
            with cols[0]:
                st.subheader(f"🔍 {item.get('query', 'N/A')}")
                st.caption(f"Category: {item.get('type', 'General')}")
            with cols[1]:
                st.write(f"**Searched At:**\n{item.get('timestamp', '')}")
            with cols[2]:
                st.write("")
                if st.button(f"Re-run", key=f"btn_{item.get('query')}_{item.get('timestamp')}"):
                    st.info(f"Loading search result for {item.get('query')}...")
                    # Add redirection logic if needed based on type
                    
    st.divider()
else:
    st.info("📌 No recent search history found. Start analyzing or comparing companies to build your history!")