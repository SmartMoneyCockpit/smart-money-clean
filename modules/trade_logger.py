
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

def main():
    st.header("📘 Trade Logger")

    symbol = st.text_input("Ticker Symbol")
    date = st.date_input("Trade Date")
    quantity = st.number_input("Quantity", step=1)
    price = st.number_input("Price", step=0.01, format="%.2f")
    notes = st.text_area("Notes")

    if st.button("Log Trade"):
        if symbol and quantity > 0 and price > 0:
            log_trade(symbol, date, quantity, price, notes)
            st.success("Trade logged to Google Sheets.")
        else:
            st.warning("Please complete all fields.")

def log_trade(symbol, date, quantity, price, notes):
    creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    client = gspread.service_account_from_dict(creds)
    config_sheet = "TradeLog"  # Could be read from config.yaml in a full app
    sheet = client.open(config_sheet).sheet1
    row = [str(date), symbol, quantity, price, notes]
    sheet.append_row(row)
