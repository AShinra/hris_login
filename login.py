import streamlit as st
from common import add_bg
from mongodb_connect.connect import connect_to_collection
from dashboard_profile import employee_profile

# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
collection = connect_to_collection('employees')

# ---------------------------------------------------------------------------
# Wrong pass
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

    # st.markdown('**:red[There was a problem]**')
    # st.markdown('**Your password is incorrect**')

    if st.button("Close", width='stretch'):
        st.rerun()


# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
def init_state():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("username", "")    

# ---------------------------------------------------------------------------
# Login window
# ---------------------------------------------------------------------------
def login_screen():

    add_bg("images/background/signin.jpg")

    left, center, right = st.columns([1, 2, 1])

    with center:
        with st.container(border=False):
            st.markdown("<h1 style='text-align:center;'>WorkMatrix</h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>🔐 Sign In</h3>", unsafe_allow_html=True)

            email = st.text_input("**Email**", placeholder="Enter your work email")
            password = st.text_input("**Password**", type="password")

            document = collection.find_one({'work_email':email})

            if st.button("Sign In", use_container_width=True):
                if document:
                    credential_id = document['credentials']
                    credential_collection = connect_to_collection('credentials_user')
                    user_credential = credential_collection.find_one({"_id":credential_id})
                    if user_credential['password']==password:
                        st.session_state.logged_in=True
                        st.rerun()
                    else:
                        dialog_signin_error('password')
                else:
                    dialog_signin_error('email')            
            





def main():
    init_state()

    if st.session_state.logged_in==True:
        employee_profile()
    else:
        login_screen()

if __name__ == "__main__":
    main()