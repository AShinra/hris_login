import streamlit as st
from common import add_bg
from mongodb_connect.connect import connect_to_collection
from dashboard import dashboard
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def replace_hashed_pass(username, new_hash):

    collection = connect_to_collection('credentials')
    
    collection.update_one(
        {"username": username},
        {"$set": {"p_hash": new_hash}})
    
    st.toast('Password updated successfully')


def pass_hasher(password):
    ph = PasswordHasher()
    return ph.hash(password)
    
def check_current_pass(username, current_pass):
    collections = connect_to_collection('credentials')
    document = collections.find_one({'username':username})
    stored_hash = document['p_hash']

    ph = PasswordHasher()

    try:
        ph.verify(stored_hash, current_pass)
    except VerifyMismatchError:
        return False
    else:
        return True

@st.dialog('Change Password')
def change_password():
    st.text_input(
        label='Username',
        key='username')
    st.text_input(
        label='Current Password',
        type='password',
        key='current_pass')
    
    if st.session_state.username not in [None, ''] and st.session_state.current_pass not in [None, '']:
        if check_current_pass(st.session_state.username, st.session_state.current_pass):
            st.text_input(
                label='New Password',
                type='password',
                key='new_pass')
            st.text_input(
                label='Confirm Password',
                type='password',
                key='confirm_pass')
            
            if st.session_state['new_pass'] not in [None, ''] and st.session_state['confirm_pass'] not in [None, '']:
                if st.session_state['new_pass'] != st.session_state['confirm_pass']:
                    st.error('New password and confirmation password do not match. Please try again.')
                else:    
                    if st.button(label="Change Password"):
                        new_hash = pass_hasher(st.session_state.new_pass)
                        replace_hashed_pass(username=st.session_state.username, new_hash=new_hash)








# ---------------------------------------------------------------------------
# Initialize MongoDB connection
# ---------------------------------------------------------------------------
collection = connect_to_collection('credentials')

# ---------------------------------------------------------------------------
# Dialog for wrong username or password
# ---------------------------------------------------------------------------
@st.dialog('Sign In error')
def dialog_signin_error(item):

    # hide title and close button
    st.markdown("""
    <style>
    /* Hide the title row */
    [data-testid="stDialog"] [role="dialog"] > div:first-child {
        display: none !important;
    }

    /* Remove the top padding from the content */
    [data-testid="stDialog"] [role="dialog"] > div:nth-child(2) {
        padding-top: 1.5rem !important;
    }
    
    /* Remove close button on the top corner */                
    [data-testid="stDialog"] [role="dialog"] > button[aria-label="Close"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # format text in the dialog
    st.markdown(
    f"""
    <div style="text-align:center;">
        <p style="margin-bottom:0; color:#d32f2f;"><b>There was a problem</b></p>
        <p><b>Your {item} is incorrect.</b></p>
    </div>
    """,
    unsafe_allow_html=True)
    
    if st.button("Close", width='stretch'):
        st.rerun()

# ---------------------------------------------------------------------------
# Dialog for enter username or password
# ---------------------------------------------------------------------------
@st.dialog('Sign In error')
def dialog_no_entry(item):

    # hide title and close button
    st.markdown("""
    <style>
    /* Hide the title row */
    [data-testid="stDialog"] [role="dialog"] > div:first-child {
        display: none !important;
    }

    /* Remove the top padding from the content */
    [data-testid="stDialog"] [role="dialog"] > div:nth-child(2) {
        padding-top: 1.5rem !important;
    }
    
    /* Remove close button on the top corner */                
    [data-testid="stDialog"] [role="dialog"] > button[aria-label="Close"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # format text in the dialog
    st.markdown(
    f"""
    <div style="text-align:center;">
        <p style="margin-bottom:0; color:#d32f2f;"><b>There was a problem</b></p>
        <p><b>Please enter your {item}.</b></p>
    </div>
    """,
    unsafe_allow_html=True)
    
    if st.button("Close", width='stretch'):
        st.rerun()



# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
def init_state():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("username", "")
    st.session_state.setdefault("document", "")

# ---------------------------------------------------------------------------
# Login window
# ---------------------------------------------------------------------------
def login_screen():

    add_bg("images/background/signin.jpg")

    left, center, right = st.columns([1, 2, 1])

    with center:
        with st.container(border=False):            

            st.markdown(f"""
                <div style="line-height:1;">
                    <p style="margin:0px 0 0 0; color:#6c757d; text-align:center; font-size:45px;">HRSync</p>
                    <p style="margin:0px 0 0 1.2; text-align:center; font-size:10px;"><strong>People. Process. Performance.</strong></p>
                    <p style="margin:0px 0 0 1.2; text-align:center; font-size:30px;"><strong>🔐 Sign In</strong><p>
                </div>
                """, unsafe_allow_html=True)

            username = st.text_input("**Username**", placeholder="Enter your username")
            password = st.text_input("**Password**", type="password")


            if st.button("Sign In", use_container_width=True):
                if not username or not password:
                    dialog_no_entry('username and password')
                else:
                    document = collection.find_one({'username':username})
                    stored_hash = document['p_hash']

                    ph = PasswordHasher()

                    try:
                        ph.verify(stored_hash, password)
                    except VerifyMismatchError:
                        dialog_signin_error('username or password')
                    else:
                        credential_id = document['_id']
                        employee_collection = connect_to_collection('employees')
                        st.session_state.logged_in=True
                        st.session_state.document=employee_collection.find_one({'credentials_id':credential_id})
                        st.rerun()
            
            cols = st.columns(2)
            with cols[0]:
                if st.button(":blue[Change Password]", type="tertiary"):
                    change_password()
            with cols[1]:
                st.markdown(f"""
                <div style="line-height:1;">
                    <p style="margin:0px 0 0 1.2; text-align:right; font-size:10px;"><strong>JMJD Solutions</strong></p>
                </div>
                """, unsafe_allow_html=True)





def main():
    init_state()    

    if st.session_state.logged_in==True:
        dashboard()
    else:
        login_screen()

if __name__ == "__main__":

    st.set_page_config(
        page_title="HRIS",
        page_icon="👥",
        layout="wide",
        initial_sidebar_state="expanded")
    
    main()