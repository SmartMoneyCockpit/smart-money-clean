
import streamlit as st
from modules import pnl_tracker, fx_exposure, smart_money_logic, trade_logger, fx_hedge_monitor, health_tracker, journal, pdf_report

st.title("📊 Smart Money Cockpit")

tabs = {
    "Jedi Theme": jedi_ui,
    "Training Tier": training,
    "PnL Tracker": pnl_tracker,
    "FX Exposure": fx_exposure,
    "Smart Money Logic": smart_money_logic,
    "Trade Logger": trade_logger,
    "FX Hedge Monitor": fx_hedge_monitor,
    "Health Tracker": health_tracker,
    "Journal": journal,
    "PDF Report": pdf_report
}

choice = st.sidebar.selectbox("Cockpit Module", list(tabs.keys()))
tabs[choice].main()
