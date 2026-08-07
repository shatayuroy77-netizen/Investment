import os
import pandas as pd
import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Investment Guide - AI Investment Workspace",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
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
st.title("📚 Investment Guide & Learning Hub")
st.write(
    "Master stock market fundamentals, valuation metrics, and AI-driven"
    " strategies step-by-step before making your investment decisions."
)

st.divider()


# ==============================
# CACHED CSV LOADER (Performance Booster)
# ==============================
@st.cache_data
def load_ticker_csv(file_path):
  return pd.read_csv(file_path, sep=",", encoding="latin-1")


# ==============================
# GLOBAL TICKER DIRECTORY SECTION (LOADED FROM CSV)
# ==============================
st.subheader(
    "🌐 Global Market Leaders & Stock Tickers (200+ Comprehensive Directory)"
)
st.write(
    "Reference directory for major global and international stock ticker"
    " symbols spanning across USA, India, Europe, and Asia-Pacific markets."
)

# Load Tickers from CSV file located in the main project directory
csv_file_path = "tickers.csv"

if os.path.exists(csv_file_path):
  try:
    # Load using the lightning-fast cached function
    df_tickers = load_ticker_csv(csv_file_path)

    # Display the dataframe in a clean, searchable, and interactive table with fixed height to prevent lagging
    st.dataframe(
        df_tickers, use_container_width=True, hide_index=True, height=400
    )
    st.info(
        "💡 **Tip:** Copy the exact ticker symbol (e.g., `ASML`, `TSM`,"
        " `RELIANCE.NS`, or `AAPL`) and paste it into the Company Analysis or"
        " Compare pages to retrieve live market data."
    )
  except Exception as e:
    st.error(f"⚠️ Error reading the `tickers.csv` file: {e}")
else:
  st.error(
      "⚠️ `tickers.csv` file not found in the main directory! Please ensure"
      " the file is saved correctly in the root project folder."
  )

st.divider()

# ==============================
# DICTIONARY DATA FOR THE LEARNING HUB (IN ENGLISH)
# ==============================
guide_data = {
    "📘 Level 1: Absolute Beginner (Must Know)": [
        {
            "term": "Stock / Share",
            "desc": "A fractional ownership unit in a corporation.",
            "why": (
                "Buying a stock means you own a small piece of the company and"
                " share in its success or failure."
            ),
        },
        {
            "term": "Stock Market",
            "desc": (
                "A centralized marketplace where shares of publicly held"
                " companies are bought and sold."
            ),
            "why": (
                "It provides liquidity, allowing buyers and investors to trade"
                " ownership securely."
            ),
        },
        {
            "term": "Investor vs. Trader",
            "desc": (
                "An investor holds assets long-term for wealth generation, while"
                " a trader aims for short-term gains via frequent buying and"
                " selling."
            ),
            "why": (
                "Knowing your style helps define your risk tolerance and time"
                " horizon."
            ),
        },
        {
            "term": "IPO (Initial Public Offering)",
            "desc": (
                "The process by which a private company offers its shares to"
                " the public for the first time."
            ),
            "why": (
                "Opens up early public investment opportunities, though often"
                " accompanied by high initial volatility."
            ),
        },
        {
            "term": "Market Capitalization (Market Cap)",
            "desc": (
                "The total dollar market value of a company's outstanding"
                " shares (Share Price × Total Shares)."
            ),
            "why": (
                "Classifies a company into large-cap, mid-cap, or small-cap,"
                " dictating its stability and risk profile."
            ),
        },
        {
            "term": "Dividend",
            "desc": (
                "A portion of corporate profits distributed to shareholders,"
                " typically in cash or additional stock."
            ),
            "why": (
                "Offers a steady passive income stream alongside potential"
                " capital appreciation."
            ),
        },
        {
            "term": "Bull vs. Bear Market",
            "desc": (
                "A bull market features rising asset prices, while a bear"
                " market signifies falling prices and widespread pessimism."
            ),
            "why": (
                "Essential for understanding macro trends and market sentiment."
            ),
        },
        {
            "term": "Volatility",
            "desc": (
                "The statistical measure of the dispersion of returns or"
                " frequency of price fluctuations for a given security."
            ),
            "why": (
                "Higher volatility indicates higher risk and potential for"
                " dramatic price swings."
            ),
        },
    ],
    "📗 Level 2: Company Analysis Terms": [
        {
            "term": "Revenue",
            "desc": (
                "The total amount of income generated by the sale of goods or"
                " services related to the company's primary operations."
            ),
            "why": "The top-line indicator of business scale and market demand.",
        },
        {
            "term": "Profit (Net Income)",
            "desc": (
                "The financial gain remaining after all operating expenses,"
                " taxes, and interest costs are subtracted from revenue."
            ),
            "why": (
                "Confirms whether the company is actually generating real"
                " earnings, not just top-line sales."
            ),
        },
        {
            "term": "Net Profit Margin",
            "desc": (
                "The percentage of revenue that turns into net income after all"
                " expenses."
            ),
            "why": (
                "Higher profit margins denote strong operational efficiency"
                " and pricing power."
            ),
        },
        {
            "term": "Business Model",
            "desc": (
                "The structural design outlining how a company creates,"
                " delivers, and captures value."
            ),
            "why": (
                "Vital for understanding how sustainable and scalable a"
                " company's revenue streams are."
            ),
        },
        {
            "term": "Economic Moat",
            "desc": (
                "A company's competitive advantage that protects its market"
                " share and long-term profitability from rivals."
            ),
            "why": (
                "Companies with a wide moat sustain high returns over long"
                " periods."
            ),
        },
        {
            "term": "Debt",
            "desc": (
                "Capital borrowed by a company from external lenders that must"
                " be repaid over time with interest."
            ),
            "why": (
                "Excessive leverage can bankrupt a company during economic"
                " downturns."
            ),
        },
    ],
    "📙 Level 3: Financial Ratios & Metrics": [
        {
            "term": "P/E Ratio (Price-to-Earnings)",
            "desc": (
                "A valuation ratio comparing a company's current share price to"
                " its per-share earnings."
            ),
            "why": (
                "High P/E can mean a stock is overvalued or has massive growth"
                " expectations; low P/E might signal an undervaluation."
            ),
        },
        {
            "term": "EPS (Earnings Per Share)",
            "desc": (
                "A company's net profit divided by the number of common shares"
                " outstanding."
            ),
            "why": (
                "Direct indicator of corporate profitability allocated to each"
                " share of stock."
            ),
        },
        {
            "term": "ROE (Return on Equity)",
            "desc": (
                "Measures financial performance by dividing net income by"
                " shareholders' equity."
            ),
            "why": (
                "High ROE indicates management is exceptionally effective at"
                " generating profit from equity financing."
            ),
        },
        {
            "term": "Debt-to-Equity (D/E) Ratio",
            "desc": (
                "Compares total corporate liabilities to shareholder equity to"
                " evaluate financial leverage."
            ),
            "why": (
                "Helps check if a company relies too heavily on dangerous"
                " levels of debt."
            ),
        },
    ],
    "📕 Level 4: Risk & Investment Concepts": [
        {
            "term": "Diversification",
            "desc": (
                "Allocating capital across multiple asset classes, industries,"
                " or stocks to minimize overall portfolio risk."
            ),
            "why": (
                "'Don't put all your eggs in one basket'—mitigates heavy losses"
                " from a single failure."
            ),
        },
        {
            "term": "Fundamental Analysis",
            "desc": (
                "Evaluating a security by attempting to measure its intrinsic"
                " value based on financial statements, management, and macro"
                " factors."
            ),
            "why": (
                "The foundation of safe, disciplined, and long-term investing."
            ),
        },
        {
            "term": "Portfolio",
            "desc": (
                "A collective grouping of financial assets held by an investor."
            ),
            "why": (
                "Tracks your absolute allocation, exposure, and net performance"
                " across assets."
            ),
        },
        {
            "term": "Red Flags",
            "desc": (
                "Warning signs in financial reports or management disclosures"
                " indicating hidden risks or malpractices."
            ),
            "why": (
                "Catching red flags early saves you from catastrophic"
                " investment losses."
            ),
        },
    ],
    "⭐ Bonus Section: AI Era & Smart Research": [
        {
            "term": "AI Investment Research",
            "desc": (
                "Leveraging artificial intelligence to parse financial filings,"
                " 10-Ks, and metrics instantly."
            ),
            "why": (
                "Transforms hours of tedious financial research into rapid,"
                " high-level insights."
            ),
        },
        {
            "term": "Investment Checklist",
            "desc": (
                "A structured sequence of validation checks executed before"
                " executing any buy or sell order."
            ),
            "why": (
                "Prevents emotional decision-making and enforces strict market"
                " discipline."
            ),
        },
    ],
}

# ==============================
# RENDER GUIDE SECTIONS
# ==============================
st.subheader("📖 Step-by-Step Learning Hub")
st.write(
    "Click on any category below to expand and learn core concepts at your own"
    " pace."
)

for category, terms_list in guide_data.items():
  with st.expander(category):
    total_items = len(terms_list)
    for i, item in enumerate(terms_list):
      bottom_margin = "16px" if i == total_items - 1 else "12px"

      st.markdown(
          f"""
                <div style="margin-top: -2px; margin-bottom:"
          f" {bottom_margin};">
                    <h3 style="font-size: 1.2rem; font-weight: 600;"
          f" margin-bottom: 2px; color: #31333F;">{item['term']}</h3>
                    <p style="margin-bottom: 4px; color: #31333F;">{item['desc']}</p>
                    <p style="margin-bottom: 0px; color: #555; font-size:"
          f" 0.95rem;"><b>Why it matters:</b> {item['why']}</p>
                </div>
            """,
          unsafe_allow_html=True,
      )

      if i < total_items - 1:
        st.markdown(
            "<hr style='margin: 12px 0px; border: none; border-top: 1px solid"
            " #e6e6e6;'>",
            unsafe_allow_html=True,
        )

st.divider()

# ==============================
# QUICK CHECKLIST FOR STOCK ANALYSIS
# ==============================
st.subheader("📊 Quick Checklist for Stock Analysis")
st.write(
    "Make sure you have verified these core checkpoints before finalizing any"
    " investment decision:"
)

col1, col2 = st.columns(2)

with col1:
  st.checkbox("Check Revenue & Profit Growth for the last 3 years")
  st.checkbox("Review Debt-to-Equity ratio to check financial stability")
  st.checkbox("Analyze Industry Competitors and Market Share")

with col2:
  st.checkbox("Evaluate Management and Leadership stability")
  st.checkbox("Check P/E Ratio and Valuation metrics")
  st.checkbox("Verify AI Research Summary & Red Flags")

# ==============================
# PAGE FOOTER / DISCLAIMER
# ==============================
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "<b>Disclaimer:</b> This workspace is designed for educational and"
    " informational purposes to assist with market research and general"
    " corporate analysis. "
    "The insights generated by the AI are for reference only and do not"
    " constitute formal financial or investment advice. "
    "Users are encouraged to perform their own due diligence or consult a"
    " qualified advisor before making financial decisions."
    "</p>",
    unsafe_allow_html=True,
)