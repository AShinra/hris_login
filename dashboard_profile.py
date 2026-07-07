import streamlit as st
from streamlit_option_menu import option_menu
from mongodb_connect.connect import connect_to_collection

def profile_data():

    st.markdown('My Profile')

    document = st.session_state.document    

    with st.container(border=True):
        cols = st.columns([1,8,1], gap="xxsmall", border=False)
        with cols[0]:
            st.markdown("""
            <style>
            [data-testid="stImage"] img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                object-fit: cover;
                border: 4px solid #ddd;
            }
            </style>
            """, unsafe_allow_html=True)

            st.image(f'images/employees/{document["employee_id"]}.jpg')

        with cols[1]:
            fname = document['first_name']
            mname = document['middle_name']
            lname = document['last_name']
            ename = document['suffix']

            fullname = " ".join(
                part for part in [fname, mname, lname, ename]
                if part)

            st.markdown(f'## **{fullname}** ##')

            employment_id = document['employment_info']
            employment_collection = connect_to_collection('employment_info')
            employment_document = employment_collection.find_one({'_id':employment_id})

            st.markdown(f"**Department**: _{employment_document['department']}_")
            st.markdown(f"**Position**: _{employment_document['position']}_")
        
        with cols[2]:
            st.button(label='✏️Edit', key='edit_1')


        
            
        




def employee_profile():

    with st.sidebar:
        profile_options = option_menu(
            menu_title="",
            options=["My Profile", "Settings"],
            icons=["person-circle", "gear"],
            default_index=0,)
    
    if profile_options=='My Profile':
        profile_data()
        
        