
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

def main():
    st.header("🩺 Health Tracker")

    bp = st.text_input("Blood Pressure (e.g., 120/80)")
    hr = st.number_input("Heart Rate (BPM)", step=1)
    sleep = st.slider("Hours Slept", 0, 12)
    notes = st.text_area("Notes")

    if st.button("Log Health"):
        if bp and hr > 0:
            log_health(bp, hr, sleep, notes)
            st.success("Health log saved to Google Sheets.")
        else:
            st.warning("Please enter all required values.")

def log_health(bp, hr, sleep, notes):
    creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    client = gspread.service_account_from_dict(creds)
    config_sheet = "HealthLog"  # Should align with config.yaml in future
    sheet = client.open(config_sheet).sheet1
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [now, bp, hr, sleep, notes]
    sheet.append_row(row)
