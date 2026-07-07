import streamlit as st
from streamlit_option_menu import option_menu
from mongodb_connect.connect import connect_to_collection

def profile_data():

    st.markdown(f"""
        <div style="line-height:1.2;">
        <h3 style="margin:0;">My Profile</h3>        
        </div>
        """, unsafe_allow_html=True)
    
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

            employment_id = document['employment_info']
            employment_collection = connect_to_collection('employment_info')
            employment_document = employment_collection.find_one({'_id':employment_id})

            st.markdown(f"""
            <div style="line-height:1.2;">
                <h2 style="margin:0;">{fullname}</h2>
                <p style="margin:4px 0 0 0;">
                    <strong>Department:</strong> <i>{employment_document['department']}</i>
                </p>
                <p style="margin:2px 0 0 0;">
                    <strong>Position:</strong> <i>{employment_document['position']}</i>
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with cols[2]:
            st.button(label='✏️Edit', key='edit_1', width='stretch')


# ---------------------------------------------------------------------------
# Personal Information Area
# ---------------------------------------------------------------------------
    st.markdown(f"""
        <div style="line-height:1.2;">
        <h4 style="margin:0;">Personal Information</h4>        
        </div>
        """, unsafe_allow_html=True)
    
    with st.container(border=True):
        cols = st.columns([2,7,1], gap="xxsmall", border=False)
        with cols[0]:
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Name</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{document['first_name']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Email Address</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{document['work_email']}</strong></p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Bio</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{employment_document['position']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Last Name</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{document['last_name']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Phone</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{document['mobile_no']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
        
        with cols[2]:
            st.button(label='✏️Edit', key='edit_2', width='stretch')

# ---------------------------------------------------------------------------
# Address Information Area
# ---------------------------------------------------------------------------
    personal_id = document['personal_info']
    personal_collection = connect_to_collection('personal_info')
    personal_document = personal_collection.find_one({'_id':personal_id})
    
    st.markdown(f"""
        <div style="line-height:1.2;">
        <h4 style="margin:0;">Address</h4>        
        </div>
        """, unsafe_allow_html=True)
    

    
    with st.container(border=True):
        cols = st.columns([2,7,1], gap="xxsmall", border=False)
        with cols[0]:
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">City</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{personal_document['current_address'][2]}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Barangay</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{personal_document['current_address'][1]}</strong></p>
                </div>
                """, unsafe_allow_html=True)        
            
            st.markdown(f"""
                <div style="line-height:1.2;">
                    <p style="margin:0px 0 0 0; color:#6c757d;">Street</p>
                    <p style="margin:0px 0 0 1.2;"><strong>{personal_document['current_address'][0]}</strong></p>
                </div>
                """, unsafe_allow_html=True)
        
        with cols[2]:
            st.button(label='✏️Edit', key='edit_3', width='stretch')
            

        
            
        




def employee_profile():

    with st.sidebar:
        profile_options = option_menu(
            menu_title="",
            options=["My Profile", "Settings"],
            icons=["person-circle", "gear"],
            default_index=0,)
    
    if profile_options=='My Profile':
        profile_data()
        
        