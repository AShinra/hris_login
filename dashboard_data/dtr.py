import streamlit as st
from common import flip_clock, validate_login
from get_time_loc import time_loc
from emp_calendar import emp_calendar
from common import validate_login

def dtr_page():
    left, right = st.columns(2, gap='xxsmall')
    with left:
        with st.container(border=True):

            st.markdown('Bundy Clock')

            flip_clock()
            cols = st.columns([1,1], gap='xxsmall')
            with cols[0]:
                if st.button(label='Time In', width='stretch'):
                    if validate_login()==True:
                        time_loc(st.session_state.document, 'login')
                    else:
                        st.toast('You are already logged in')
            with cols[1]:
                if st.button(label='Time Out', width='stretch'):
                    time_loc(st.session_state.document, 'logout')


    with right:
        # st.write(st.session_state.document)
        emp_calendar()