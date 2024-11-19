import page_process as pp
import streamlit as st

pp.page_initialize()
tab1, tab2 = st.tabs(["Top and Recommend Businesses", "I'm Feeling Lucky"])

with tab1:
    pp.page_top10_business()
    pp.page_user_recommend()

with tab2:
    pp.page_business_predict()
