from streamlit_calendar import calendar
import streamlit as st

def emp_calendar():
    events = [
        {
            "title": "Login",
            "start": "2026-07-12T08:00:00",
            "end": "2026-07-12T17:00:00",
            "backgroundColor": "#4CAF50",
            "borderColor": "#4CAF50",
        },
        {
            "title": "Leave",
            "start": "2026-07-15",
            "allDay": True,
            "backgroundColor": "#F44336",
        },
    ]

    options = {
        "initialView": "dayGridMonth",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay,listWeek",
        },
        "editable": False,
        "selectable": True,
    }

    state = calendar(events=events, options=options)

    # st.write(state)