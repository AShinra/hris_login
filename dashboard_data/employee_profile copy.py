import streamlit as st
from mongodb_connect.connect import connect_to_collection
from mongodb_connect.connect import get_personal_info, get_employment_info, get_government_benefit_info


def profile_data():

    # initialize data
    document = st.session_state.document
    
    personal_info_id = document['personal_info_id']
    personal_info_document = get_personal_info(personal_info_id)
    
    employment_info_id = document['employment_info_id']
    employment_document = get_employment_info(employment_info_id)
    
    government_benefit_id = document['government_benefit_id']
    government_benefit_document = get_government_benefit_info(government_benefit_id)
    
    with st.container(border=False):
        cols = st.columns([2,8], gap="xxsmall", border=False)
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

            _address = []
            for k, v in personal_info_document["current_address"].items():
                _address.append(v)           
            
            current_address = ", ".join(part for part in _address if part)

            st.markdown(f"""
            <div style="line-height:1.0;">
                <p style="margin:0; font-size:40px;"><strong>{fullname}</strong></p>
                <p style="margin:0; font-size:20px;">{document['employee_id']} | {employment_document['position']}</p>
                <p style="margin:0; font-size:20px;">{employment_document['department']}</p>
                <p style="margin:0; font-size:15px; color:#6c757d;">🏠 {current_address}</p>
                <p style="margin:0; font-size:15px; color:#6c757d;">📱{document['mobile_no']}</p>
                <p style="margin:0 0 0 1; font-size:15px; color:#6c757d;">✉️{document['work_email']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with st.expander('Expand Information', expanded=False):
        cols = st.columns([1,1], gap="xxsmall", border=False)
        with cols[0]:
            st.markdown("""
            <style>
            table, tbody, tr, td, th {
                border: none !important;
                border-collapse: collapse !important;
                padding:1px 0 !important;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <table style="width:100%; border-collapse:collapse; font-size:15px;">
                    <tr>
                        <td style="font-size:20px; color:#429E9D;"><strong><u>Bio</u></strong></td>
                    </tr>
                    <tr>
                        <td style="width:60%;"><strong>Gender</strong></td>
                        <td><strong>{personal_info_document['gender']}</strong></td>
                    </tr>
                    <tr>
                        <td style="width:30%;"><strong>Birth Date</strong></td>
                        <td style><strong>{personal_info_document['date_of_birth'].strftime('%b %d, %Y')}</strong></td>
                    </tr>
                    <tr>
                        <td style="width:60%;"><strong>Birth Place</strong></td>
                        <td><strong>{personal_info_document['place_of_birth']}</strong></td>
                    </tr>
                    <tr>
                        <td style="width:60%;"><strong>Civil Status</strong></td>
                        <td><strong>{personal_info_document['civil_status']}</strong></td>
                    </tr>
                    <tr>
                        <td style="width:60%;"><strong>Nationality</strong></td>
                        <td><strong>{personal_info_document['nationality']}</strong></td>
                    </tr>
                    <tr>
                        <td style="width:60%;"><strong>Blood Type</strong></td>
                        <td><strong>{personal_info_document['blood_type']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%; font-size:20px; color:#429E9D;"><strong><u>Permanent Address</u></strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>House Number</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['house_no']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Street</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['street']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Subdivision</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['subdivision']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Barangay</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['barangay']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>City</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['city_municipality']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Province</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['province']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Region</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['region']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Postal Code</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['postal_code']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Country</strong></td>
                        <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['country']}</strong></td>
                    </tr>
                </table>
                """, unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("""
            <style>
            table, tbody, tr, td, th {
                border: none !important;
                border-collapse: collapse !important;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <table style="width:100%; border-collapse:collapse; font-size:15px;">
                    <tr>
                        <td style="font-size:20px; color:#429E9D;"><strong><u>Work Info</u></strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Status</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['employment_status']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Employment</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['employment_type']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Manager</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['manager']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Supervisor</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['supervisor']}</strong></td>
                    </tr>
                    <tr>
                        <td style="font-size:20px; color:#429E9D;"><strong><u>Govt ID Numbers</u></strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Social Security Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['sss']['sss_number']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>PhilHealth Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['philhealth']['philhealth_number']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Pag-IBIG Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['pagibig']['pagibig_mid']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Tax Identification Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['tax']['tin']}</strong></td>
                    </tr>
                </table>
                """, unsafe_allow_html=True)
            
            with st.expander(f'**:blue[Emergency Contact]**'):
                st.markdown(f"""
                <table style="width:100%; border-collapse:collapse; font-size:15px;">
                    <tr>
                        <td style="font-size:20px; color:#429E9D;"><strong><u>Work Info</u></strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Status</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['employment_status']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Employment</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['employment_type']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Manager</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['manager']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:60%;"><strong>Supervisor</strong></td>
                        <td style="padding:4px 0;"><strong>{employment_document['supervisor']}</strong></td>
                    </tr>
                    <tr>
                        <td style="font-size:20px; color:#429E9D;"><strong><u>Govt ID Numbers</u></strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Social Security Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['sss']['sss_number']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>PhilHealth Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['philhealth']['philhealth_number']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Pag-IBIG Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['pagibig']['pagibig_mid']}</strong></td>
                    </tr>
                    <tr>
                        <td style="padding:4px 0; width:30%;"><strong>Tax Identification Number</strong></td>
                        <td style="padding:4px 0;"><strong>{government_benefit_document['tax']['tin']}</strong></td>
                    </tr>
                </table>
                """, unsafe_allow_html=True)
        

            