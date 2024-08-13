import streamlit as st

def home_page():
    st.title("eKYC using Computer Vision")
    st.write("""
        Welcome to the eKYC application! This project consists of two main modules:
        1. **Data Extraction**: Upload an image of a CNIC card to extract data.
        2. **Face Comparison**: Upload an image of a CNIC card and another image of the person to verify if they match.
    """)
