import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation
from geopy.geocoders import Nominatim
from datetime import datetime
from logs import employee_log
from common import update_credentials
from uuid import uuid4


# ---------------------------------------------------------------------------
# Auth — replace this with your real authentication (DB lookup, OAuth, etc.).
# Never hard-code real credentials in production; use secrets/env vars.
# ---------------------------------------------------------------------------
CREDENTIALS = {
    "admin": "password123",
    "ronald": "letmein",
}


def check_credentials(username: str, password: str) -> bool:
    return CREDENTIALS.get(username) == password


# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
def init_state():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("username", "")


# ---------------------------------------------------------------------------
# Login screen
# ---------------------------------------------------------------------------
def login_screen():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password.")


# ---------------------------------------------------------------------------
# Main app — shown only after login. Captures the user's location.
# ---------------------------------------------------------------------------
@st.dialog('Time and Location')
def time_loc(item, type):

    time_loc_data = []

    st.markdown(f'''
        <div style="line-height:1.0; width:100%;">
            <p>
                <span>
                    Welcome,&nbsp;
                </span>
                <span>
                    <strong>{st.session_state.document['first_name']}</strong>
                </span>
            </p>
            <p>
                <span>
                    Click the icon to&nbsp;
                </span>
                <span style="color:red;">
                    <strong>{type.title()}</strong>
                </span>
            </p>
        </div>
    ''', unsafe_allow_html=True)

    # The component renders its own button. Call it directly and check the
    # coordinate values — a dict full of None is still truthy.
    location = streamlit_geolocation()

    if location and location.get("latitude") is not None:
        latitude = location["latitude"]
        longitude = location["longitude"]

        geolocator = Nominatim(user_agent="hris_app")

        try:
            location = geolocator.reverse(
                (latitude, longitude),
                language="en",
                exactly_one=True)
        except:
            pass
        else:
            loc_data = {"address": location.address,
                        "latitude": location.latitude,
                        "longitude": location.longitude,
                        "raw": location.raw}


            # _time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # st.write(_time)
            # st.map(pd.DataFrame({"lat": [latitude], "lon": [longitude]}))

            time_loc_data.append(loc_data)
            _date = datetime.now()
            time_loc_data.append(_date)
            session_number = str(uuid4())
            update_credentials(session_number, _date)

            st.markdown(f'''
                <div style="line-height:1.0; width:100%;">
                    <p><strong>Location</strong></p>
                    <p style="color:blue;">{loc_data["address"]}</p>
                    <p><strong>Time</strong></p>
                    <p style="color:blue;">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                </div>
            ''', unsafe_allow_html=True)

            # st.markdown(f'**:red[Location]**: {loc_data["address"]}')
            # st.markdown(f'**:red[Date and Time]**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            with st.expander('Location Viewer'):
                st.map(pd.DataFrame({"lat": [latitude], "lon": [longitude]}))

            employee_log(time_loc_data, type, session_number)
    else:
        st.info("Waiting for location — click the icon above and allow access.")

    