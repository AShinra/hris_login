import streamlit as st
from streamlit_option_menu import option_menu
from common import flip_clock
from get_time_loc import time_loc
from dashboard_data.employee_profile import profile_data
from dashboard_data.dtr import dtr_page
from mongodb_connect.connect import connect_to_collection
from dashboard_data.admin import page_overview


def dashboard():

    # credentials_id = st.session_state.document['credentials_id']
    # collection = connect_to_collection('credentials')
    # credentials_doc = collection.find_one({'_id':credentials_id})
    
    role_id = st.session_state.cred_document['role']
    collection = connect_to_collection('roles')
    role_doc = collection.find_one({'_id':role_id})
    role = role_doc['role']    

    if role=='user':
        options = ["My Profile", "DTR", "Settings", "Logout"]
        icons = ["person-circle", "clock", "gear", "door-open"]
    elif role=='administrator':
        options = ["Overview", "Attendance Summary", "Leave Management", "Logout"]
        icons = ["speedometer2", "calendar-check-fill", "calendar-event-fill", "door-open"]

    with st.sidebar:
        
        profile_options = option_menu(
            menu_title="",
            options=options,
            icons=icons,
            default_index=0,)
    
    if profile_options=='My Profile':
        profile_data()
    elif profile_options=='DTR':
        dtr_page()
    elif profile_options=='Settings':
        ''''''
    elif profile_options=='Overview':
        page_overview()
    elif profile_options=='Logout':
        st.session_state.logged_in=False
        st.session_state.document=None
        st.rerun()
        
        