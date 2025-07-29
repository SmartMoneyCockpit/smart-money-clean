
import streamlit as st
import gspread
import json
import os
from datetime import datetime

def main():
    st.header("🩺 Health Tracker")

    bp = st.text_input("Blood Pressure (e.g., 120/80)")
    hr = st.number_input("Heart Rate (BPM)", step=1)
    sleep = st.slider("Hours Slept", 0, 12)
    notes = st.text_area("Notes (Optional)")

    if st.button("Submit Health Log"):
        if bp and hr:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = [now, bp, hr, sleep, notes]
            if push_to_sheets("HealthLog", row):
                st.success("✅ Health data logged.")
            else:
                st.error("❌ Failed to log health data.")
        else:
            st.warning("Please enter BP and HR.")

def push_to_sheets(sheet_name, row_data):
    try:
        creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        client = gspread.service_account_from_dict(creds)
        sheet = client.open(sheet_name).sheet1
        sheet.append_row(row_data)
        return True
    except Exception as e:
        print("Google Sheets error:", e)
        return False
