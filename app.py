
import streamlit as st
from modules import (
    pnl_tracker, fx_exposure, smart_money_logic, trade_logger,
    fx_hedge_monitor, health_tracker, journal, pdf_report,
    jedi_ui, training
)

st.set_page_config(page_title="Smart Money Cockpit", layout="wide")

st.title("📊 Smart Money Cockpit")

tabs = {
    "PnL Tracker": pnl_tracker,
    "FX Exposure": fx_exposure,
    "Smart Money Logic": smart_money_logic,
    "Trade Logger": trade_logger,
    "FX Hedge Monitor": fx_hedge_monitor,
    "Health Tracker": health_tracker,
    "Journal": journal,
    "PDF Report": pdf_report,
    "Jedi Theme": jedi_ui,
    "Training Tier": training
}

choice = st.sidebar.selectbox("📂 Select a Module", list(tabs.keys()))
tabs[choice].main()
