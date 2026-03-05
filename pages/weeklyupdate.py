import streamlit as st

st.set_page_config(page_title="Farmlog")
st.title("Weekly updates")
st.header("updates regarding pests,ph and other cases")
if st.button("Now let's move on to the final expense report"):
    st.switch_page("pages/expense.py")
