import streamlit as st
from get_time_loc import time_loc

def dtr_page():
    st.markdown(f"""
        <div style="line-height:1.2;">
        <h3 style="margin:0;">Daily Time Record</h3>        
        </div>
        """, unsafe_allow_html=True)
    
    with st.container(border=True):
        if st.button(label='Time In'):
            time_loc('Time In')