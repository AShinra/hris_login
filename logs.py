from mongodb_connect.connect import connect_to_collection
import streamlit as st

def employee_log(time_loc_data, type, session_number):

    document = st.session_state.document

    obj_id = document['_id'] 
    employee_id = document['employee_id']

    collection = connect_to_collection('employee_logs')
    
    log = {
        'user':document['_id'],
        'type':type,
        'date':time_loc_data[1],
        'location':time_loc_data[0]['address'],
        'employee_id':document['employee_id'],
        'session_number':session_number
    }
    
    result = collection.insert_one(log)
    