import streamlit as st
import gspread
import json
import os
from datetime import date

def main():
    st.header("📘 Trade Logger")

    ticker = st.text_input("Ticker Symbol")
    trade_date = st.date_input("Trade Date", value=date.today())
    quantity = st.number_input("Quantity", step=1, format="%d")
    price = st.number_input("Price", step=0.01, format="%.2f")
    notes = st.text_area("Notes (Optional)")

    if st.button("Submit Trade"):
        if ticker and quantity and price:
            row = [str(trade_date), ticker.upper(), quantity, price, notes]
            result = push_to_sheets("COCKPIT", "TradeLog", row)
            if result is True:
                st.success(f"✅ Trade for {ticker.upper()} logged successfully.")
            else:
                st.error("❌ Failed to log trade.")
                st.exception(result)  # Display the actual error for debugging
        else:
            st.warning("Please complete all required fields.")

def push_to_sheets(sheet_name, tab_name, row_data):
    try:
        creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        client = gspread.service_account_from_dict(creds)
        sheet = client.open(sheet_name).worksheet(tab_name)
        sheet.append_row(row_data)
        return True
    except Exception as e:
        return e
