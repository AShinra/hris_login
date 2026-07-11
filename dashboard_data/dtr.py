import streamlit as st
from common import flip_clock
from get_time_loc import time_loc























def dtr_page():
    left, right = st.columns(2, gap='xxsmall')
    with left:
        with st.container(border=True):

            st.markdown('Bundy Clock')

            flip_clock()
            cols = st.columns([1,1], gap='xxsmall')
            with cols[0]:
                if st.button(label='Time In', width='stretch'):
                    time_loc(st.session_state.document)
            with cols[1]:
                st.button(label='Time Out', width='stretch')
            
    



    with right:
        st.markdown(f"""
            <div style="
                background: white;
                border: 1px solid #E2E8F0;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,.06);
                margin-bottom: 20px;">
                <div>
                    "Bundy Clock"
                </div>
            </div>""", unsafe_allow_html=True)