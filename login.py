import streamlit as st
from common import add_bg

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

            username = st.text_input("**Username**")
            password = st.text_input("**Password**", type="password")

            if st.button("Sign In", use_container_width=True):
                pass




def main():
    init_state()

    login_screen()

    # if st.session_state.logged_in==True:
    #     location_screen()
    # else:
    #     login_screen()

if __name__ == "__main__":
    main()