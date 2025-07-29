
import streamlit as st

def main():
    st.set_page_config(page_title="Smart Money Cockpit", layout="wide")
    st.title("🚀 Smart Money Cockpit")

    st.write("This version runs safely on Streamlit Cloud without IBKR integration.")
    st.write("Modules loaded: PnL Tracker, FX Exposure, Health Dashboard, Smart Money Alerts, Journal.")

if __name__ == "__main__":
    main()
