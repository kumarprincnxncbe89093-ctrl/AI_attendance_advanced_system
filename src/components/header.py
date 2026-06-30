import streamlit as st
import base64

def header_home():
    with open("logo.png", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <div class="home-hero">
            <img src="data:image/png;base64,{encoded}" class="home-logo"/>
            <div class="ai-eyebrow">Neural recognition workflow</div>
            <h1>AI Attendance<br>Recognition</h1>
            <p>Face recognition, voice matching, subject enrollment, and attendance records in a neural style transfer inspired interface.</p>
        </div>
        <style>
            .home-hero {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0.2rem 0 1.8rem;
                color: white;
            }}

            .home-hero .home-logo {{
                width: 108px;
                height: 108px;
                object-fit: contain;
                margin-bottom: 1rem;
                border-radius: 0.5rem;
                border: 1px solid rgba(255,255,255,0.14);
                background: rgba(30,41,59,0.6);
                box-shadow: 0 25px 50px -20px rgba(0,0,0,0.65);
            }}

            .home-hero h1 {{
                text-align: center;
                color: #ffffff !important;
                text-shadow: 0 18px 40px rgba(0,0,0,0.42);
                font-size: 3.5rem !important;
            }}

            .home-hero p {{
                color: #cbd5e1 !important;
                max-width: 720px;
                text-align: center;
                font-size: 1.08rem;
                line-height: 1.7;
            }}

            @media (max-width: 760px) {{
                .home-hero {{
                    margin: 0.15rem 0 1.4rem;
                }}

                .home-hero .home-logo {{
                    width: 82px;
                    height: 82px;
                    margin-bottom: 0.7rem;
                }}

                .home-hero h1 {{
                    font-family: 'Outfit', sans-serif !important;
                    font-size: 2rem !important;
                    line-height: 1.08 !important;
                    color: #ffffff !important;
                    letter-spacing: 0 !important;
                    text-shadow: 0 6px 16px rgba(26, 32, 88, 0.18);
                }}
            }}

            @media (max-height: 760px) {{
                .home-hero {{
                    margin-bottom: 1.5rem;
                }}

                .home-hero .home-logo {{
                    width: 92px;
                    height: 92px;
                    margin-bottom: 0.75rem;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():
    with open("logo.png", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <div class="dashboard-brand">
            <img src="data:image/png;base64,{encoded}" class="dashboard-logo"/>
            <h2>AI Attendance<br>Studio</h2>
        </div>
        <style>
            .dashboard-brand {{
                display: flex;
                align-items: center;
                justify-content: flex-start;
                gap: 12px;
                background: linear-gradient(145deg, rgba(30,41,59,0.72), rgba(15,23,42,0.72));
                border: 1px solid rgba(255,255,255,0.12);
                border-radius: 0.5rem;
                padding: 0.75rem 1rem;
                box-shadow: 0 25px 50px -28px rgba(0,0,0,0.65);
            }}

            .dashboard-logo {{
                width: 72px;
                height: 72px;
                object-fit: contain;
                margin-bottom: 0;
                border-radius: 0.5rem;
            }}

            .dashboard-brand h2 {{
                text-align: left;
                color: #f8fafc !important;
                text-shadow: 0 10px 28px rgba(0,0,0,0.45);
            }}

            @media (max-width: 760px) {{
                .dashboard-brand {{
                    justify-content: flex-start;
                    gap: 8px;
                }}

                .dashboard-logo {{
                    width: 72px;
                    height: 72px;
                    margin-bottom: 10px;
                }}

                .dashboard-brand h2 {{
                    font-family: 'Outfit', sans-serif !important;
                    font-size: 1.45rem !important;
                    line-height: 1.05 !important;
                    color: #f8fafc !important;
                    letter-spacing: 0 !important;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
