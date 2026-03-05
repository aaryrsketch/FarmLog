import streamlit as st
import os
st.image(os.path.join(os.getcwd(),"static","bgw.jpg"))
st.divider()
st.set_page_config(page_title="farmlog")
st.title("Farmlog")
st.header("Simplify Track Thrive")
st.markdown("your one stop personalized farm data organization site")
if st.button ("lets begin"):
    st.switch_page("pages/datastart.py")

