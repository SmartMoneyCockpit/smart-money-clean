
import streamlit as st

def main():
    st.header("🧘 Jedi Theme Settings")
    mode = st.radio("Choose Your Path:", ["Subtle", "Bold"])
    if mode == "Subtle":
        st.success("Subtle Jedi mode activated. Clean and elegant.")
    else:
        st.warning("Bold Jedi mode activated. Prepare for full immersion.")
