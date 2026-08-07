import streamlit as st
from utils import get_company_profile, get_stock_quote, generate_ai_research, generate_word_report

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Company Analysis - AI Investment Research",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# SIDEBAR NAVIGATION (Consistent)
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
st.title("🔎 Company Analysis Workspace")
st.write("Search using official stock ticker symbols to generate a structured AI research report powered by live financial metrics and corporate analysis.")

st.divider()

# ==============================
# SEARCH SECTION (Ticker-Only Optimized UX)
# ==============================
st.subheader("Enter Stock Ticker Symbol")

# Strong warning added
st.warning("⚠️ **Strict Rule:** Please enter official **stock ticker symbols only** (e.g., `AAPL`, `MSFT`, `RELIANCE.NS`). **DO NOT** type full company names.")

col1, col2 = st.columns([3, 1])

with col1:
    company_input = st.text_input(
        "Enter Stock Ticker Symbol",
        placeholder="DON'T TYPE FULL NAME (e.g., type AAPL, NOT Apple)",
        label_visibility="collapsed"
    )

with col2:
    st.write("") # Alignment spacing
    st.write("")
    analyze_btn = st.button("🚀 Analyze Company", use_container_width=True)

# ==============================
# SESSION STATE INITIALIZATION FOR HISTORY
# ==============================
if "recent_searches" not in st.session_state:
    st.session_state.recent_searches = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# ==============================
# ANALYSIS LOGIC & REAL-TIME API INTEGRATION
# ==============================
if analyze_btn:
    if company_input.strip() == "":
        st.warning("Please enter a valid stock ticker symbol before analyzing.")
    else:
        ticker = company_input.strip().upper()
        
        # --- SMART CHARACTER LENGTH & FORMAT VALIDATION ---
        MAX_TICKER_LENGTH = 12
        
        # Check if ticker exceeds character limit or contains spaces (full name check)
        if len(ticker) > MAX_TICKER_LENGTH or " " in ticker:
            st.error(f"❌ **Invalid Input:** '{company_input}' is too long or contains spaces. Please enter an official **stock ticker symbol only** (Max 12 characters, e.g., `AAPL`, `RELIANCE.NS`). Full company names are not accepted.")
        else:
            # Proceed to API call only if validation passes
            search_entry = {"ticker": ticker, "name": ticker}
            if search_entry not in st.session_state.recent_searches:
                st.session_state.recent_searches.insert(0, search_entry)
                if len(st.session_state.recent_searches) > 10:
                    st.session_state.recent_searches.pop()
            
            # Loading & Fetching Real-Time Data from Utils
            with st.spinner(f"Fetching financial data and generating Gen AI research for {ticker}..."):
                profile = get_company_profile(ticker)
                quote = get_stock_quote(ticker)
                
                # Extract real company name if available from Finnhub profile
                company_name = profile.get("name", ticker) if profile else ticker
                
                # Generate AI Research Report using Gemini
                ai_report = generate_ai_research(company_name, ticker, profile)
            
            st.success(f"Analysis report generated successfully for {company_name} ({ticker})!")
            
            # Action Bar (Favorite Button)
            col_fav, col_share = st.columns([1, 5])
            with col_fav:
                fav_item = {"ticker": ticker, "name": company_name, "report": ai_report}
                if fav_item not in st.session_state.favorites:
                    if st.button("Add to Favorites"):
                        st.session_state.favorites.append(fav_item)
                        st.success("Added to favorites!")
                else:
                    st.info("Already in Favorites")

            st.divider()

            # ==============================
            # LIVE MARKET METRICS (Finnhub Data)
            # ==============================
            if quote and "c" in quote:
                st.subheader("Live Market Data")
                
                # Safe helper to prevent NoneType formatting errors
                def safe_float(val):
                    try:
                        return float(val) if val is not None else 0.0
                    except (ValueError, TypeError):
                        return 0.0

                c_price = safe_float(quote.get('c'))
                d_change = safe_float(quote.get('d'))
                dp_change = safe_float(quote.get('dp'))
                h_price = safe_float(quote.get('h'))
                l_price = safe_float(quote.get('l'))

                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Current Price", f"${c_price:.2f}")
                m2.metric("Daily Change", f"${d_change:.2f}", f"{dp_change:.2f}%")
                m3.metric("Day High", f"${h_price:.2f}")
                m4.metric("Day Low", f"${l_price:.2f}")
                st.divider()

            # ==============================
            # REPORT TABS LAYOUT
            # ==============================
            st.header(f"Research Report: {company_name} ({ticker})")
            
            tab1, tab2, tab3, tab4 = st.tabs(["Overview & Business", "Financial Profile", "Corporate Details", "AI Research & Red Flags"])
            
            with tab1:
                st.subheader("Company Overview")
                if profile:
                    st.write(f"**Country:** {profile.get('country', 'N/A')}")
                    st.write(f"**Industry:** {profile.get('finnhubIndustry', 'N/A')}")
                    st.write(f"**Exchange:** {profile.get('exchange', 'N/A')}")
                    st.write(f"**Currency:** {profile.get('currency', 'USD')}")
                    if profile.get('weburl'):
                        st.markdown(f"**Official Website:** [{profile.get('weburl')}]({profile.get('weburl')})")
                else:
                    st.info("Basic profile data is currently limited for this specific ticker.")

            with tab2:
                st.subheader("Advanced Financial Metrics & Valuation")
                if profile:
                    col_p1, col_p2, col_p3, col_p4 = st.columns(4)
                    col_p1.metric("Market Capitalization", f"${profile.get('marketCapitalization', 0) or 0:,.2f}M")
                    col_p2.metric("Shares Outstanding", f"{profile.get('shareOutstanding', 0) or 0:,.2f}M")
                    col_p3.metric("P/E Ratio (Est.)", f"{profile.get('peRatio', 'N/A')}")
                    col_p4.metric("Debt-to-Equity", f"{profile.get('debtToEquity', 'N/A')}")
                else:
                    st.info("Detailed financial metrics unavailable.")

            with tab3:
                st.subheader("Raw Corporate Profile Data")
                if profile:
                    st.json(profile)
                else:
                    st.warning("No corporate profile data returned from the API.")

            with tab4:
                # Top row inside tab4: Subheader on left, Word Download button on right
                c_head, c_btn = st.columns([4, 1])
                with c_head:
                    st.subheader("AI Investment Research & Risk Assessment")
                with c_btn:
                    st.write("") # Spacing alignment
                    word_data = generate_word_report(company_name, ticker, ai_report)
                    st.download_button(
                        label="📥 Download Word (.docx)",
                        data=word_data,
                        file_name=f"{ticker}_Research_Report.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
                
                st.markdown(ai_report)
                
                st.divider()
                st.markdown("### Key Risk Assessment Checklist (Red Flags)")
                chk1, chk2 = st.columns(2)
                with chk1:
                    st.checkbox("High Debt-to-Equity / Leverage Risk checked")
                    st.checkbox("Declining Profit Margins checked")
                with chk2:
                    st.checkbox("Regulatory / Legal Headwinds checked")
                    st.checkbox("Corporate Governance / Management Risk checked")

else:
    # Empty State: Only single clean helper box when no search is performed yet
    st.info("Tip: Enter an official stock ticker symbol above (e.g., AAPL, RELIANCE.NS) and click Analyze Company to generate a live AI research report. (Need a ticker? Check the Investment Guide page!)")

# ==============================
# FOOTER
# ==============================
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; color: gray; font-size: 14px;">
    AI Investment Research Workspace  |  Python  •  Streamlit  •  Gemini  •  Finnhub
    </div>
    """,
    unsafe_allow_html=True
)