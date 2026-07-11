import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

def bg_markdown(item):
    st.markdown(
    f"""
    <div style="
        background-color:#000000;
        color:white;
        padding:0px 12px;
        border-radius:6px;
        text-align:left;
        width:100%;
        box-sizing:border-box;
    ">
        {item}
    </div>
    """,
    unsafe_allow_html=True)

def add_bg(image_file):
    # Resolve relative to this file so it works no matter where Streamlit is launched from
    image_path = Path(image_file)
    if not image_path.is_absolute():
        image_path = (Path(__file__).parent / image_path).resolve()

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        /* Hide Streamlit header */
        header {{
            visibility: hidden;
        }}

        /* Hide collapsed sidebar button */
        [data-testid="collapsedControl"] {{
            display: none;
        }}

        /* Background */
        .stApp {{
            background: url("data:image/{image_path.suffix[1:]};base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Center everything */
        .main > div {{
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        /* Glass card */
        .login-card {{
            width: 420px;
            padding: 40px;
            border-radius: 20px;

            background: rgba(255,255,255,.18);

            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);

            border:1px solid rgba(255,255,255,.25);

            box-shadow:0 10px 35px rgba(0,0,0,.30);
        }}

        h1,h3 {{
            text-align:center;
            color:white;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

def flip_clock():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        background: transparent;
    }

    .container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }

    .clock {
        display: flex;
        gap: 1px;
        font-family: 'Arial Black', sans-serif;
    }
    .digit {
        background: linear-gradient(#333, #000);
        color: white;
        font-size: 30px;
        padding: 10px 10px;
        border-radius: 8px;
        box-shadow: inset 0 -4px 0 rgba(0,0,0,0.4);
    }
    .colon {
        font-size: 30px;
        color: white;
        padding-top: 10px;
    }
    </style>
    </head>

    <body>
    <div class="container">
        <div class="clock">
            <div class="digit" id="h1">0</div>
            <div class="digit" id="h2">0</div>
            <div class="colon">:</div>
            <div class="digit" id="m1">0</div>
            <div class="digit" id="m2">0</div>
            <div class="colon">:</div>
            <div class="digit" id="s1">0</div>
            <div class="digit" id="s2">0</div>
        </div>
    </div>

    <script>
    function updateClock() {
        const now = new Date();
        const h = String(now.getHours()).padStart(2,'0');
        const m = String(now.getMinutes()).padStart(2,'0');
        const s = String(now.getSeconds()).padStart(2,'0');
        const t = h + m + s;

        ["h1","h2","m1","m2","s1","s2"].forEach((id,i)=>{
            document.getElementById(id).innerText = t[i];
        });
    }

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    </body> 
    </html>
    """
    
    components.html(html, height=120)