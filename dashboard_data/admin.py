import streamlit as st
from mongodb_connect.connect import connect_to_collection

def insert_logo():
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

    st.image(f"images/background/company/company_logo.jpg")


def employee_count():
    collection = connect_to_collection('employees')
    return collection.count_documents({"first_name":{"$ne": "Administrator"}})


def horizontal_cards(count, items):

    insert_logo()

    cols = st.columns(count, gap="xxsmall")

    for i in range(count):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background:#8dc1ee;
                padding:5px;
                border-radius:12px;
                border:1px solid #ffffff;
                box-shadow:0 2px 8px rgba(0,0,0,.08);
                text-align:center;
            ">
                <div style="font-size:28px;">{items[i][1]}</div>
                <div style="font-size:14px;color:#000000;">{items[i][0]}</div>
                <div style="font-size:32px;font-weight:700;color:#000000;">{items[i][2]}</div>
            </div>
            """, unsafe_allow_html=True)



def page_overview():

    # insert logo


    # generate overview cards

    emp_count = employee_count()

    items = [
        ['Total Employees', '👥', emp_count],
        ['Today Present', '🟢', 300],
        ['On Leave', '🟡', 25],
        ['Pending Approvals', '⏳', 10]]
    
    count = len(items)

    horizontal_cards(count=count, items=items)
    
    
    