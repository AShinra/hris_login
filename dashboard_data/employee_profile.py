import streamlit as st
from mongodb_connect.connect import connect_to_collection
from mongodb_connect.connect import get_personal_info, get_employment_info, get_government_benefit_info


def info_card(title, items, icon):

    rows = ""

    for label, value in items.items():
        rows += f"""
        <div style="display:flex; justify-content:space-between;">
            <span style="color:#6B7280";><i class="bi {value[1]}" style="color:#6366F1; margin-right:8px;"></i>{label}</span>
            <span style="color:#111827";>{value[0]}</span>
        </div>"""

    st.markdown(f"""
            <div style="
                        background: #8dc1ee;
                        border: 1px solid #E2E8F0;
                        border-radius: 10px;
                        padding: 10px;
                        box-shadow: 0 4px 12px rgba(0,0,0,.06);
                        margin-bottom: 20px;">
                <div>
                    <i class="bi {icon}" style="color:blue; font-size:25px;"></i>
                    <b style="color:#ffffff; font-size:20px;">{title}</b>
                </div>
                    <div style="
                    background: #FAFAFF;
                    border: 1px solid #E0E7FF;
                    border-radius: 5px;
                    padding: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,.06);
                    margin-bottom: 10px;">
                        {rows}
                    </div>
                </div>""", unsafe_allow_html=True)
    

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



    tabs = st.tabs(["**Personal Info**", "**Employment Info**", "**Contact Info**", "**Government Info**"])
    with tabs[0]:
        left, right = st.columns(2)
        with left:
            p = personal_info_document
            info_card(
                "Bio Info",
                {
                    "Gender": [p["gender"], "bi-gender-ambiguous"],
                    "Birth Date": [p["date_of_birth"].strftime("%b %d, %Y"), "bi-calendar-event-fill"],
                    "Birth Place": [p["place_of_birth"], "bi-geo-alt-fill"],
                    "Civil Status": [p["civil_status"], "bi-person-hearts"],
                    "Nationality": [p["nationality"], "bi-flag-fill"],
                    "Blood Type": [p["blood_type"], "bi-droplet-fill"],
                }, 'bi-person-fill'
            )
        
        with right:
            pa = personal_info_document['permanent_address']
            info_card(
                "Permanent Address",
                {
                    "House Number": [pa['house_no'], "bi-house-door-fill"],
                    "Street": [pa["street"], "bi-signpost-2-fill"],
                    "Subdivision": [pa["subdivision"], "bi-buildings-fill"],
                    "Barangay": [pa["barangay"], "bi-buildings-fill"],
                    "City": [pa["city_municipality"], "bi-building-fill"],
                    "Province": [pa["province"], "bi-map-fill"],
                    "Region": [pa["region"], "bi-globe-asia-australia"],
                    "Country": [pa["country"], "bi-globe"],
                    "Postal Code": [pa["postal_code"], "bi-mailbox"],
                }, 'bi-person-fill'
            )

    with tabs[1]:
        left, right = st.columns(2)
        with left:
            e = employment_document
            info_card(
                "Employement",
                {
                    "Date Hired": [e["date_hired"].strftime("%b %d, %Y"), 'bi-calendar-check-fill'],
                    "Status": [e["employment_status"], 'bi-check-circle-fill'],
                    "Type": [e["employment_type"], 'bi-person-workspace'],
                    "Department": [e["department"], 'bi-diagram-3-fill'],
                    "Position": [e["position"], 'bi-briefcase-fill'],
                    "Manager": [e["manager"], 'bi-person-badge-fill'],
                    "Supervisor": [e["supervisor"], 'bi-person-check-fill'],
                    "Arrangement": [e["work_arrangement"], 'bi-laptop-fill'],
                    "Shift": [f'{e["shift_schedule"][0]} to {e["shift_schedule"][1]}', 'bi-clock-history'],
                }, 'bi-buildings-fill'
            )        
    
    with tabs[2]:
        left, right = st.columns(2)
        with left:
            p = personal_info_document
            pc = personal_info_document["contact_address"]
            info_card(
                "Contacts",
                {
                    "Person": [p["contact_person"], "bi-person-vcard-fill"],
                    "Relationship": [p["relationship"], "bi-people-fill"],
                    "Number": [p["contact_no"], "bi-telephone-fill"],
                    "House No.": [pc['house_no'], "bi-house-door-fill"],
                    "Street": [pc['street'], "bi-signpost-2-fill"],
                    "Subdivision": [pc['subdivision'], "bi-buildings-fill"],
                    "Barangay": [pc['barangay'], "bi-buildings-fill"],
                    "City": [pc['city_municipality'], "bi-building-fill"],
                    "Province": [pc['province'], "bi-map-fill"],
                    "Region": [pc['region'], "bi-globe-asia-australia"],
                    "Country": [pc['country'], "bi-globe"],
                    "Postal Code": [pc['postal_code'], "bi-mailbox"],
                }, 'bi-person-lines-fill'
            )
    
    with tabs[3]:
        left, right = st.columns(2)
        with left:
            sss = government_benefit_document['sss']
            info_card(
                "Social Security System",
                {
                    "Number": [sss["sss_number"], 'bi-person-vcard-fill'],
                    "Status": [sss["membership_type"], 'bi-check-circle-fill'],
                    "Contribution.": [sss["contribution_type"], 'bi-cash-stack'],
                    "Effectivity.": [sss["effectivity_date"], 'bi-calendar-check-fill'],
                }, 'bi-dash-circle-dotted'
            )
            pi = government_benefit_document['pagibig']
            info_card(
                "PagIBIG",
                {
                    "Number": [pi["pagibig_mid"], 'bi-person-vcard-fill'],
                    "Status": [pi["membership_status"], 'bi-check-circle-fill'],
                    "Effectivity.": [pi["effectivity_date"], 'bi-calendar-check-fill'],
                }, 'bi-dash-circle-dotted'
            )

        
        with right:
            phic = government_benefit_document['philhealth']
            info_card(
                "PhilHealth",
                {
                    "Number": [phic["philhealth_number"], 'bi-person-vcard-fill'],
                    "Status": [phic["membership_type"], 'bi-check-circle-fill'],
                    "Contribution.": [phic["contribution_type"], 'bi-cash-stack'],
                    "Effectivity.": [phic["effectivity_date"], 'bi-calendar-check-fill'],
                }, 'bi-dash-circle-dotted'
            )

            bir = government_benefit_document['tax']
            info_card(
                "Bureau of Internal Revenue",
                {
                    "dot Number": [bir["tin"], 'bi-person-vcard-fill'],
                    "Status": [bir["tax_status"], 'bi-check-circle-fill'],
                    "RDO": [bir["registered_rdo"], 'bi-person-vcard-fill'],
                }, 'bi-dash-circle-dotted'
            )