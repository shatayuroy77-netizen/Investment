import streamlit as st
import yfinance as yf

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Favorites - AI Investment Workspace",
    page_icon="⭐",
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
st.title("⭐ Favorite Companies")
st.write(
    "Quickly access your saved companies and bookmarked investment research"
    " reports."
)

st.divider()

# ==============================
# INITIALIZE SESSION STATE FOR FAVORITES
# ==============================
if "favorites" not in st.session_state:
  # Using a set or list to store unique tickers. Let's use a list/set.
  # Pre-populating with a couple of real defaults if empty, or keeping it strictly dynamic.
  st.session_state["favorites"] = ["AAPL", "MSFT", "TSLA"]

# ==============================
# RENDER FAVORITES CONTENT
# ==============================
favorite_tickers = st.session_state.get("favorites", [])

if favorite_tickers:
  st.success(
      f"You have {len(favorite_tickers)} saved favorite company ticker(s)."
  )

  # Add an option to clear or manage favorites
  col_ctrl1, col_ctrl2 = st.columns([3, 1])
  with col_ctrl2:
    if st.button("🗑️ Clear All Favorites", use_container_width=True):
      st.session_state["favorites"] = []
      st.rerun()

  st.divider()

  for ticker in favorite_tickers:
    clean_ticker = ticker.strip().upper()
    with st.container(border=True):
      cols = st.columns([3, 2, 2])

      # Fetch basic info live via yfinance for each favorite
      try:
        stock = yf.Ticker(clean_ticker)
        info = stock.info
        name = info.get("longName", clean_ticker)
        sector = info.get("sector", "N/A")
        market_cap = info.get("marketCap", "N/A")

        # Get latest price if available
        hist = stock.history(period="1d")
        current_price = (
            f"${hist['Close'].iloc[-1]:.2f}" if not hist.empty else "N/A"
        )
      except Exception:
        name = clean_ticker
        sector = "N/A"
        current_price = "N/A"

      with cols[0]:
        st.subheader(f"{name} (`{clean_ticker}`)")
        st.caption(f"Sector: {sector} | Current Price: **{current_price}**")

      with cols[1]:
        market_cap_str = (
            f"${market_cap:,}"
            if isinstance(market_cap, (int, float))
            else "N/A"
        )
        st.write(f"**Market Cap:**\n{market_cap_str}")

      with cols[2]:
        st.write("")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
          if st.button("🔎 Analyze", key=f"view_{clean_ticker}"):
            st.info(
                f"Go to 'Company Analysis' and search for `{clean_ticker}` to"
                " view full reports."
            )
        with col_btn2:
          if st.button("❌ Remove", key=f"rem_{clean_ticker}"):
            st.session_state["favorites"].remove(ticker)
            st.rerun()
else:
  st.info(
      "📌 You haven't added any companies to your favorites yet. Go to"
      " 'Company Analysis' to bookmark companies."
  )

# ==============================
# PAGE FOOTER / DISCLAIMER
# ==============================
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "<b>Disclaimer:</b> This workspace is for educational and research"
    " purposes only. "
    "It does not constitute financial or investment advice."
    "</p>",
    unsafe_allow_html=True,
)