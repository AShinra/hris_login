import streamlit as st
from common import add_bg
from mongodb_connect.connect import connect_to_collection
from dashboard import dashboard

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
                    document = collection.find_one({'username':username, 'password':password})

                    if document:
                        credential_id = document['_id']
                        employee_collection = connect_to_collection('employees')
                        st.session_state.logged_in=True
                        st.session_state.document=employee_collection.find_one({'credentials_id':credential_id})
                        st.rerun()
                    else:
                        dialog_signin_error('username or password')
                    
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