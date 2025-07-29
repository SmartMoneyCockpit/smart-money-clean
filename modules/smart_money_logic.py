
import streamlit as st
import gspread
import pandas as pd
import json
import os

def main():
    st.image("static/assets/coin.png", width=80)
    st.header("🧠 Smart Money Logic Scanner")
    try:
        creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        client = gspread.service_account_from_dict(creds)
        sheet = client.open("COCKPIT").worksheet("TradeLog")
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No trade data found yet.")
            return

        st.subheader("📋 Trade Summary")
        st.dataframe(df.tail(10), use_container_width=True)

        st.subheader("🧠 Signal Assessment")
        df['Signal'] = df.apply(analyze_trade, axis=1)
        for idx, row in df.tail(10).iterrows():
            st.markdown(f"**{row['Ticker']}** | Qty: {row['Quantity']} | ${row['Price']} | Note: _{row['Notes']}_")
            st.markdown(row['Signal'])
            st.markdown("---")
    except Exception as e:
        st.error("Failed to load Smart Money logic.")
        st.exception(e)

def analyze_trade(row):
    notes = str(row.get("Notes", "")).lower()
    qty = row.get("Quantity", 0)
    price = row.get("Price", 0)
    if "sweep" in notes or "breakout" in notes:
        return "🟢 **Smart Money Aligned** – Strategy keyword found"
    elif qty < 10 or price < 5:
        return "🔴 **Weak Trade** – Too small or low liquidity"
    elif "review" in notes or "watch" in notes:
        return "🟡 **Neutral** – Marked for review"
    else:
        return "⚪ No signal"
