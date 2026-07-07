import streamlit as st
from mongodb_connect.connect import connect_to_collection
from mongodb_connect.connect import get_personal_info, get_employment_info, get_government_benefit_info


def profile_data():

    st.markdown(f"""
        <div style="line-height:1.2;">
        <h3 style="margin:0;">My Profile</h3>        
        </div>
        """, unsafe_allow_html=True)
    
    document = st.session_state.document    

    with st.container(border=True):
        cols = st.columns([1,3,3,3], gap="xxsmall", border=False)
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
            lname = document['last_name']
            
            fullname = ", ".join(
                part for part in [lname, fname]
                if part)

            employment_id = document['employment_info_id']
            employment_collection = connect_to_collection('employment_info')
            employment_document = employment_collection.find_one({'_id':employment_id})

            personal_id = document['personal_info_id']
            personal_collection = connect_to_collection('personal_info')
            personal_document = personal_collection.find_one({'_id':personal_id})

            st.markdown(f"""
            <div style="line-height:1.0;">
                <p style="margin:0; font-size:40px;"><strong>{fullname}</strong></p>
                <p style="margin:0; font-size:20px;">{document['employee_id']} | {employment_document['position']}</p>
                <p style="margin:0; font-size:20px;">{employment_document['department']}</p>
                <p style="margin:0; font-size:15px; color:#6c757d;">Address: {", ".join(personal_document['current_address'])}</p>
                <p style="margin:0; font-size:15px; color:#6c757d;">{document['mobile_no']}</p>
                <p style="margin:0; font-size:15px; color:#6c757d;">{document['work_email']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with cols[2]:

            try:
                government_benefit_id = document['government_benefit_id']
                government_benefit_document = get_government_benefit_info(government_benefit_id)

                col = st.columns([2,8], gap='xxsmall', border=False)
                with col[0]:
                    st.markdown(f"""
                    <div style="line-height:1.0;">
                        <p style="margin:0; font-size:15px; color:#6c757d;">SSS:</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">PHIC:</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">HDMF:</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">TIN:</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col[1]:
                    st.markdown(f"""
                    <div style="line-height:1.0;">
                        <p style="margin:0; font-size:15px; color:#6c757d;">{government_benefit_document['sss']['sss_number']}</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">{government_benefit_document['philhealth']['philhealth_number']}</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">{government_benefit_document['pagibig']['pagibig_mid']}</p>
                        <p style="margin:0; font-size:15px; color:#6c757d;">{government_benefit_document['tax']['tin']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            except:
                st.write('Updating this section for government benefits...')

        with cols[3]:
            st.write('Updating this section for leave credits and other information...')