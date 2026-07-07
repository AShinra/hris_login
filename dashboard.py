import streamlit as st
from streamlit_option_menu import option_menu
from common import flip_clock
from get_time_loc import time_loc
from dashboard_data.employee_profile import profile_data
from dashboard_data.dtr import dtr_page


def dashboard():

    with st.sidebar:
        
        # display the flip clock on sidebar
        flip_clock()

        profile_options = option_menu(
            menu_title="",
            options=["My Profile", "DTR", "Settings", "Logout"],
            icons=["person-circle", "clock", "gear", "door-open"],
            default_index=0,)
    
    if profile_options=='My Profile':
        profile_data()
    elif profile_options=='DTR':
        dtr_page()
    elif profile_options=='Settings':
        ''''''
    elif profile_options=='Logout':
        st.session_state.logged_in=False
        st.session_state.document=None
        st.rerun()
        
        