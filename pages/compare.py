import io
import pandas as pd
from fpdf import FPDF
import streamlit as st
import yfinance as yf
from google import genai
import os

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Compare Companies - AI Investment Workspace",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Gemini Client
client = genai.Client()

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
st.title("⚖️ Compare Companies")
st.write(
    "Compare multiple companies side-by-side based on their live market metrics, valuation, and institutional AI analysis."
)

st.divider()

# ==============================
# QUICK PRESET SELECTOR
# ==============================
st.markdown("### Quick Preset Pairs")
st.write("Click any preset below to instantly fill the comparison inputs:")

preset_col1, preset_col2, preset_col3, preset_col4 = st.columns(4)

if "comp_1" not in st.session_state:
    st.session_state.comp_1 = ""
if "comp_2" not in st.session_state:
    st.session_state.comp_2 = ""
if "run_comparison" not in st.session_state:
    st.session_state.run_comparison = False

with preset_col1:
    if st.button("Apple vs Microsoft"):
        st.session_state.comp_1 = "AAPL"
        st.session_state.comp_2 = "MSFT"

with preset_col2:
    if st.button("Google vs Meta"):
        st.session_state.comp_1 = "GOOGL"
        st.session_state.comp_2 = "META"

with preset_col3:
    if st.button("TCS vs Infosys"):
        st.session_state.comp_1 = "TCS.NS"
        st.session_state.comp_2 = "INFY.NS"

with preset_col4:
    if st.button("NVIDIA vs AMD"):
        st.session_state.comp_1 = "NVDA"
        st.session_state.comp_2 = "AMD"

st.divider()

# ==============================
# COMPANY SELECTION INPUTS
# ==============================
col1, col2 = st.columns(2)

with col1:
    company_1 = st.text_input(
        "First Company",
        value=st.session_state.comp_1,
        placeholder="e.g., AAPL, TCS.NS...",
    )

with col2:
    company_2 = st.text_input(
        "Second Company",
        value=st.session_state.comp_2,
        placeholder="e.g., MSFT, INFY.NS...",
    )

st.session_state.comp_1 = company_1
st.session_state.comp_2 = company_2

if st.button("🚀 Run Comparison"):
    st.session_state.run_comparison = True

st.divider()

# ==============================
# COMPARISON VIEW & LIVE DATA FETCHING
# ==============================
if st.session_state.run_comparison:
    c1 = st.session_state.comp_1.strip().upper()
    c2 = st.session_state.comp_2.strip().upper()

    if not c1 or not c2:
        st.warning("Please enter or select both company ticker symbols.")
    elif c1 == c2:
        st.warning("Please enter two different companies for comparison.")
    else:
        with st.spinner(f"Fetching live financial data and generating AI analysis for {c1} and {c2}..."):
            try:
                stock1 = yf.Ticker(c1)
                stock2 = yf.Ticker(c2)

                info1 = stock1.info
                info2 = stock2.info

                name1 = info1.get("longName", c1)
                name2 = info2.get("longName", c2)

                sector1 = info1.get("sector", "N/A")
                sector2 = info2.get("sector", "N/A")

                mcap1 = info1.get("marketCap", 0)
                mcap2 = info2.get("marketCap", 0)

                pe1 = info1.get("trailingPE", "N/A")
                pe2 = info2.get("trailingPE", "N/A")

                # Get latest price
                hist1 = stock1.history(period="1d")
                hist2 = stock2.history(period="1d")

                price1 = hist1["Close"].iloc[-1] if not hist1.empty else "N/A"
                price2 = hist2["Close"].iloc[-1] if not hist2.empty else "N/A"

                # Generate AI Comparative Insight using Gemini 2.5/3.5 Flash
                ai_prompt = f"""
                You are a senior institutional equity research analyst. Provide an exhaustive, critical, and institutional-grade comparative analysis between two companies:
                1. Company A: {name1} ({c1}), Sector: {sector1}, Market Cap: ${mcap1:,}, P/E: {pe1}
                2. Company B: {name2} ({c2}), Sector: {sector2}, Market Cap: ${mcap2:,}, P/E: {pe2}

                Structure your analysis with the following sections using Markdown:
                ### 1. Executive Comparison & Valuation Verdict
                ### 2. Business Model & Economic Moat Face-off
                ### 3. Financial Performance & Capital Efficiency
                ### 4. Key Risks & Headwinds Comparison
                ### 5. Final Institutional Recommendation (Which one offers better risk-adjusted return?)
                """

                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=ai_prompt,
                )
                ai_analysis = response.text

            except Exception as e:
                st.error(f"⚠️ Error fetching data or generating AI analysis: {e}")
                st.stop()

        st.success(f"Successfully compared **{name1} ({c1})** vs **{name2} ({c2})**")

        # Layout for comparison overview
        comp_col1, comp_col2 = st.columns(2)

        with comp_col1:
            st.subheader(f"{name1} (`{c1}`)")
            st.write(f"**Sector:** {sector1}")
            st.metric(
                label="Current Price",
                value=f"${price1:.2f}" if isinstance(price1, (int, float)) else price1,
            )
            st.metric(
                label="Market Cap",
                value=f"${mcap1:,}" if isinstance(mcap1, (int, float)) else "N/A",
            )
            st.metric(
                label="Trailing P/E Ratio",
                value=f"{pe1:.2f}" if isinstance(pe1, (int, float)) else pe1,
            )

        with comp_col2:
            st.subheader(f"{name2} (`{c2}`)")
            st.write(f"**Sector:** {sector2}")
            st.metric(
                label="Current Price",
                value=f"${price2:.2f}" if isinstance(price2, (int, float)) else price2,
            )
            st.metric(
                label="Market Cap",
                value=f"${mcap2:,}" if isinstance(mcap2, (int, float)) else "N/A",
            )
            st.metric(
                label="Trailing P/E Ratio",
                value=f"{pe2:.2f}" if isinstance(pe2, (int, float)) else pe2,
            )

        st.divider()

        # Render AI Comparative Analysis
        st.markdown("### 🤖 AI Institutional Comparative Analysis")
        st.markdown(ai_analysis)

        st.divider()

        # ==============================
        # REPORT DOWNLOAD OPTIONS (PDF)
        # ==============================
        st.markdown("### Export Research Report")

        def create_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "AI Investment Research Companion", ln=True, align="C")
            pdf.set_font("Arial", "I", 12)
            pdf.cell(0, 10, f"Live Comparison Report: {c1} vs {c2}", ln=True, align="C")
            pdf.ln(10)

            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"1. {name1} ({c1}) Metrics:", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 8, f"- Sector: {sector1}\n- Current Price: ${price1}\n- Market Cap: ${mcap1}\n- Trailing P/E: {pe1}")
            pdf.ln(5)

            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"2. {name2} ({c2}) Metrics:", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 8, f"- Sector: {sector2}\n- Current Price: ${price2}\n- Market Cap: ${mcap2}\n- Trailing P/E: {pe2}")
            
            return bytes(pdf.output())

        pdf_bytes = create_pdf()

        st.download_button(
            label="📄 Download Live PDF Report",
            data=pdf_bytes,
            file_name=f"comparison_{c1}_vs_{c2}.pdf",
            mime="application/pdf",
        )

else:
    st.info("Please select a preset pair or enter custom tickers (e.g., `TCS.NS`, `AAPL`), then click 'Run Comparison' to view the live market analysis and AI report.")