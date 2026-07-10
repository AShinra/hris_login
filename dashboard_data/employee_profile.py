import streamlit as st
from mongodb_connect.connect import connect_to_collection
from mongodb_connect.connect import get_personal_info, get_employment_info, get_government_benefit_info


# def info_card(title, items):

#     rows = ""

#     for label, value in items.items():
#         rows += f"""
#         <div style="display:flex; justify-content:space-between;">
#             <span><i class="bi bi-person-fill" style="color:blue; margin-right:8px;"></i>{label}</span>
#             <span>{value}</span>
#         </div>
#         """

#     st.markdown(f"""
#             <div style="
#                         background: white;
#                         border: 1px solid #E2E8F0;
#                         border-radius: 10px;
#                         padding: 10px;
#                         box-shadow: 0 4px 12px rgba(0,0,0,.06);
#                         margin-bottom: 20px;">
#                 <div>
#                     <i class="bi bi-person" style="color:blue; font-size:25px;"></i>
#                     <b style="color:blue; font-size:20px;">Bio</b>
#                     <div style="
#                     background: white;
#                     border: 1px solid #E2E8F0;
#                     border-radius: 5px;
#                     padding: 10px;
#                     box-shadow: 0 4px 12px rgba(0,0,0,.06);
#                     margin-bottom: 10px;">
#                         <div style="display:flex; justify-content:space-between;">
#                             <span><i class="bi bi-person-fill" style="color:blue; margin-right:8px;"></i>{title}</span>
#                             <span>{value}</span>
#                         </div>
#                     </div>
#                 </div>
#             </div>""", unsafe_allow_html=True)



def profile_data():

    st.markdown("""
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    """, unsafe_allow_html=True)

    # initialize data
    document = st.session_state.document
    
    personal_info_id = document['personal_info_id']
    personal_info_document = get_personal_info(personal_info_id)
    
    employment_info_id = document['employment_info_id']
    employment_document = get_employment_info(employment_info_id)
    
    government_benefit_id = document['government_benefit_id']
    government_benefit_document = get_government_benefit_info(government_benefit_id)

    # compute the values
    fname = document['first_name']
    lname = document['last_name']
    
    fullname = ", ".join(
        part for part in [lname, fname]
        if part)

    _address = []
    for k, v in personal_info_document["current_address"].items():
        _address.append(v)           
    
    current_address = ", ".join(part for part in _address if part)

    st.markdown("""
        <style>

        .employee-card{
            background:white;
            border-radius:18px;
            border:1px solid #E2E8F0;
            padding:25px;
            box-shadow:0 4px 15px rgba(0,0,0,.08);
        }

        .photo-card{
            background:#EEF5FF;
            border:1px solid #D6E4FF;
            border-radius:18px;
            padding:20px;
            text-align:center;
        }

        .info-card{
            background:#F8FAFC;
            border-radius:18px;
            padding:15px 25px;
        }

        .name{
            font-size:38px;
            font-weight:700;
            color:#1E293B;
            margin-bottom:2px;
        }

        .position{
            font-size:20px;
            color:#2563EB;
            font-weight:600;
        }

        .department{
            font-size:18px;
            color:#64748B;
        }

        .details{
            font-size:15px;
            color:#64748B;
            margin-top:12px;
            line-height:1.0;
        }

        .status{
            background:#DCFCE7;
            color:#15803D;
            padding:5px 14px;
            border-radius:50px;
            font-size:14px;
            font-weight:bold;
        }

        </style>
        """, unsafe_allow_html=True)
    
    # st.markdown('<div class="employee-card">', unsafe_allow_html=True)

    photo, info = st.columns([2,8])

    with photo:

        # st.markdown('<div class="photo-card">', unsafe_allow_html=True)

        st.markdown("""
        <style>
        [data-testid="stImage"] img{
            width:140px;
            height:140px;
            border-radius:50%;
            object-fit:cover;
            border:5px solid white;
            box-shadow:0 4px 12px rgba(0,0,0,.15);
            margin:auto;
        }
        </style>
        """, unsafe_allow_html=True)

        st.image(f"images/employees/{document['employee_id']}.jpg")

        # st.markdown("</div>", unsafe_allow_html=True)

    with info:

        st.markdown(f"""
        <div class="info-card">

        <div style="display:flex;justify-content:space-between;align-items:center;">

        <div>

        <div class="name">{fullname}</div>

        <div class="position">
            {document['employee_id']} • {employment_document['position']}
        </div>
        <div class="department">
            {employment_document['department']}
        </div>

        </div>

        <div class="status">
            ACTIVE
        </div>

        </div>

        <div class="details">

        📍 {current_address}<br>

        📱 {document['mobile_no']}<br>

        ✉ {document['work_email']}

        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <style>

    .info-card{
        background:white;
        border:1px solid #E2E8F0;
        border-radius:16px;
        padding:20px;
        box-shadow:0 2px 8px rgba(0,0,0,.05);
        margin-bottom:0px;
    }

    .info-title{
        color:#2563EB;
        font-size:22px;
        font-weight:700;
        margin-bottom:15px;
    }

    .info-row{
        display:flex;
        justify-content:space-between;
        padding:10px 0;
        border-bottom:1px solid #F1F5F9;
    }

    .info-row:last-child{
        border-bottom:none;
    }

    .info-label{
        color:#64748B;
        font-weight:600;
    }

    .info-value{
        color:#0F172A;
        font-weight:600;
        text-align:right;
    }

    </style>
    """, unsafe_allow_html=True)



    tabs = st.tabs(["**Personal Info**", "**Employment Info**", "**Contact Info**"])
    with tabs[0]:
        left, right = st.columns(2)
        with left:
            st.markdown(f"""
            <div style="
                        background: white;
                        border: 1px solid #E2E8F0;
                        border-radius: 10px;
                        padding: 10px;
                        box-shadow: 0 4px 12px rgba(0,0,0,.06);
                        margin-bottom: 20px;">
                <div>
                    <i class="bi bi-person" style="color:blue; font-size:25px;"></i>
                    <b style="color:blue; font-size:20px;">Bio</b>
                    <div style="
                    background: white;
                    border: 1px solid #E2E8F0;
                    border-radius: 5px;
                    padding: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,.06);
                    margin-bottom: 10px;">
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-person-fill" style="color:blue; margin-right:8px;"></i>Gender</span>
                            <span>{personal_info_document["gender"]}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-calendar3" style="color:blue; margin-right:8px;"></i>Birth Date</span>
                            <span>{personal_info_document["date_of_birth"].strftime('%b %d, %Y')}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-geo-alt-fill" style="color:blue; margin-right:8px;"></i>Birth Place</span>
                            <span>{personal_info_document["place_of_birth"]}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-heart-fill" style="color:blue; margin-right:8px;"></i>Civil Status</span>
                            <span>{personal_info_document["civil_status"]}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-flag-fill" style="color:blue; margin-right:8px;"></i>Nationality</span>
                            <span>{personal_info_document["nationality"]}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-droplet-fill" style="color:blue; margin-right:8px;"></i>Blood Type</span>
                            <span>{personal_info_document["blood_type"]}</span>
                        </div>
                    </div>
                </div>
            </div>
        
            """, unsafe_allow_html=True)
        
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
                    <i class="bi bi-person" style="color:green; font-size:25px;"></i>
                    <b style="color:green; font-size:20px;">Permanent Address</b>
                    <div style="
                    background: white;
                    border: 1px solid #E2E8F0;
                    border-radius: 5px;
                    padding: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,.06);
                    margin-bottom: 10px;">
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-person-fill" style="color:green; margin-right:8px;"></i>House Number</span>
                            <span>{personal_info_document['permanent_address']['house_no']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-signpost-2-fill" style="color:green; margin-right:8px;"></i>Street</span>
                            <span>{personal_info_document['permanent_address']['street']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-houses-fill" style="color:green; margin-right:8px;"></i>Subdivision</span>
                            <span>{personal_info_document['permanent_address']['subdivision']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-people-fill" style="color:green; margin-right:8px;"></i>Barangay</span>
                            <span>{personal_info_document['permanent_address']['barangay']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-buildings-fill" style="color:green; margin-right:8px;"></i>City</span>
                            <span>{personal_info_document['permanent_address']['city_municipality']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-map-fill" style="color:green; margin-right:8px;"></i>Province</span>
                            <span>{personal_info_document['permanent_address']['province']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-map-fill" style="color:green; margin-right:8px;"></i>Region</span>
                            <span>{personal_info_document['permanent_address']['region']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-envelope-fill" style="color:green; margin-right:8px;"></i>Postal Code</span>
                            <span>{personal_info_document['permanent_address']['postal_code']}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span><i class="bi bi-globe2" style="color:green; margin-right:8px;"></i>Country</span>
                            <span>{personal_info_document['permanent_address']['country']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


            # info_card(
            #     "Bio",
            #     {
            #         "Gender": personal_info_document["gender"],
            #         "Birth Date": personal_info_document["date_of_birth"].strftime("%b %d, %Y"),
            #         "Birth Place": personal_info_document["place_of_birth"],
            #         "Civil Status": personal_info_document["civil_status"],
            #         "Nationality": personal_info_document["nationality"],
            #         "Blood Type": personal_info_document["blood_type"],
            #     },
            #     "🧑"
            # )

    #     with right:

    #         p = personal_info_document["permanent_address"]

    #         info_card(
    #             "Permanent Address",
    #             {
    #                 "House No": p["house_no"],
    #                 "Street": p["street"],
    #                 "Subdivision": p["subdivision"],
    #                 "Barangay": p["barangay"],
    #                 "City": p["city_municipality"],
    #                 "Province": p["province"],
    #                 "Postal Code": p["postal_code"],
    #                 "Country": p["country"],
    #             },
    #             "🏠"
    #         )
    
    # with tab2:

    #     left, right = st.columns(2)

    #     with left:

    #         info_card(
    #             "Employment",
    #             {
    #                 "Status": employment_document["employment_status"],
    #                 "Type": employment_document["employment_type"],
    #                 "Department": employment_document["department"],
    #                 "Position": employment_document["position"],
    #                 "Manager": employment_document["manager"],
    #                 "Supervisor": employment_document["supervisor"],
    #             },
    #             "💼"
    #         )

    #     with right:

    #         info_card(
    #             "Government IDs",
    #             {
    #                 "SSS": government_benefit_document["sss"]["sss_number"],
    #                 "PhilHealth": government_benefit_document["philhealth"]["philhealth_number"],
    #                 "Pag-IBIG": government_benefit_document["pagibig"]["pagibig_mid"],
    #                 "TIN": government_benefit_document["tax"]["tin"],
    #             },
    #             "🪪"
    #         )

    















    # tabs = st.tabs(['Personal Info', 'Employment Info'])
    # with tabs[0]:
    # # with st.expander('Expand Information', expanded=False):
    #     cols = st.columns([1,1], gap="xxsmall", border=False)
    #     with cols[0]:
    #         st.markdown("""
    #         <style>
    #         table, tbody, tr, td, th {
    #             border: none !important;
    #             border-collapse: collapse !important;
    #             padding:1px 0 !important;
    #         }
    #         </style>
    #         """, unsafe_allow_html=True)

    #         st.markdown(f"""
    #             <table style="width:100%; border-collapse:collapse; font-size:15px;">
    #                 <tr>
    #                     <td style="background-color:#dee2e6; font-size:20px; color:#429E9D;"><strong><u>Bio</u></strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:60%;"><strong>Gender</strong></td>
    #                     <td style="background-color:#dee2e6;"><strong>{personal_info_document['gender']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:30%;"><strong>Birth Date</strong></td>
    #                     <td style><strong>{personal_info_document['date_of_birth'].strftime('%b %d, %Y')}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:60%;"><strong>Birth Place</strong></td>
    #                     <td><strong>{personal_info_document['place_of_birth']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:60%;"><strong>Civil Status</strong></td>
    #                     <td><strong>{personal_info_document['civil_status']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:60%;"><strong>Nationality</strong></td>
    #                     <td><strong>{personal_info_document['nationality']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="width:60%;"><strong>Blood Type</strong></td>
    #                     <td><strong>{personal_info_document['blood_type']}</strong></td>
    #                 </tr>
    #                 </table>
    #                 """, unsafe_allow_html=True)
            
    #         with st.expander('**:blue[Emergency Contact Info]**'):
    #             st.markdown(f"""
    #             <table style="width:100%; border-collapse:collapse; font-size:15px;">
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Status</strong></td>
    #                     <td style="padding:4px 0;"><strong>{employment_document['employment_status']}</strong></td>
    #                 </tr>
    #             </table>
    #             """, unsafe_allow_html=True)

    #     with cols[1]:
    #         st.markdown("""
    #         <style>
    #         table, tbody, tr, td, th {
    #             border: none !important;
    #             border-collapse: collapse !important;
    #             padding:1px 0 !important;
    #         }
    #         </style>
    #         """, unsafe_allow_html=True)

    #         st.markdown(f"""
    #             <table style="width:100%; border-collapse:collapse; font-size:15px;">
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%; font-size:20px; color:#429E9D;"><strong><u>Permanent Address</u></strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>House Number</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['house_no']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Street</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['street']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Subdivision</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['subdivision']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Barangay</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['barangay']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>City</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['city_municipality']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Province</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['province']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Region</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['region']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Postal Code</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['postal_code']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Country</strong></td>
    #                     <td style="padding:4px 0;"><strong>{personal_info_document['permanent_address']['country']}</strong></td>
    #                 </tr>
    #             </table>
    #             """, unsafe_allow_html=True)

    # with tabs[1]:
    #     cols = st.columns([1,1], gap="xxsmall", border=False)
    #     with cols[0]:
    #         st.markdown("""
    #         <style>
    #         table, tbody, tr, td, th {
    #             border: none !important;
    #             border-collapse: collapse !important;
    #         }
    #         </style>
    #         """, unsafe_allow_html=True)

    #         st.markdown(f"""
    #             <table style="width:100%; border-collapse:collapse; font-size:15px;">
    #                 <tr>
    #                     <td style="font-size:20px; color:#429E9D;"><strong><u>Work Info</u></strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Status</strong></td>
    #                     <td style="padding:4px 0;"><strong>{employment_document['employment_status']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Employment</strong></td>
    #                     <td style="padding:4px 0;"><strong>{employment_document['employment_type']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Manager</strong></td>
    #                     <td style="padding:4px 0;"><strong>{employment_document['manager']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Supervisor</strong></td>
    #                     <td style="padding:4px 0;"><strong>{employment_document['supervisor']}</strong></td>
    #                 </tr>
    #             </table>
    #             """, unsafe_allow_html=True)

    #     with cols[1]:
    #         st.markdown("""
    #         <style>
    #         table, tbody, tr, td, th {
    #             border: none !important;
    #             border-collapse: collapse !important;
    #         }
    #         </style>
    #         """, unsafe_allow_html=True)

    #         st.markdown(f"""
    #             <table style="width:100%; border-collapse:collapse; font-size:15px;">
    #                 <tr>
    #                     <td style="font-size:20px; color:#429E9D;"><strong><u>Government ID Nos.</u></strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:60%;"><strong>Social Security Number</strong></td>
    #                     <td style="padding:4px 0;"><strong>{government_benefit_document['sss']['sss_number']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>PhilHealth Number</strong></td>
    #                     <td style="padding:4px 0;"><strong>{government_benefit_document['philhealth']['philhealth_number']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Pag-IBIG Number</strong></td>
    #                     <td style="padding:4px 0;"><strong>{government_benefit_document['pagibig']['pagibig_mid']}</strong></td>
    #                 </tr>
    #                 <tr>
    #                     <td style="padding:4px 0; width:30%;"><strong>Tax Identification Number</strong></td>
    #                     <td style="padding:4px 0;"><strong>{government_benefit_document['tax']['tin']}</strong></td>
    #                 </tr>
    #             </table>
    #             """, unsafe_allow_html=True)
        
        