import streamlit as st

def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background:
                        linear-gradient(rgba(11, 18, 32, 0.88), rgba(11, 18, 32, 0.95)),
                        radial-gradient(circle at 14% 18%, rgba(14, 165, 233, 0.24), transparent 30%),
                        radial-gradient(circle at 84% 16%, rgba(244, 114, 182, 0.16), transparent 28%),
                        radial-gradient(circle at 48% 94%, rgba(34, 197, 94, 0.12), transparent 30%),
                        #0b1220 !important;
                    color: #e2e8f0 !important;
                }

                .block-container {
                    max-width: 1180px !important;
                    padding-top: 1rem !important;
                    padding-bottom: 1rem !important;
                }

                .stApp div[data-testid="stHorizontalBlock"] {
                    align-items: stretch;
                    gap: 1.4rem;
                }

                .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) {
                    background:
                        linear-gradient(145deg, rgba(15, 23, 42, 0.86), rgba(30, 41, 59, 0.78)),
                        radial-gradient(circle at 16% 10%, rgba(14, 165, 233, 0.16), transparent 36%);
                    border: 1px solid rgba(148, 163, 184, 0.2);
                    border-radius: 0.5rem;
                    padding: 1.25rem !important;
                    box-shadow: 0 24px 52px -30px rgba(0,0,0,0.72);
                    backdrop-filter: blur(16px);
                }

                .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) h2 {
                    color: #ffffff !important;
                    font-size: clamp(1.45rem, 2vw, 1.85rem) !important;
                    margin: 0.35rem 0 0.8rem !important;
                    line-height: 1.2 !important;
                }

                .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) p {
                    color: #ffffff !important;
                }

                .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) img {
                    margin: 0.2rem 0 1.2rem 0;
                    filter: drop-shadow(0 18px 26px rgba(0, 0, 0, 0.38));
                }

                .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) button {
                    margin-top: 0.25rem;
                    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.28);
                }

                @media (max-width: 760px) {
                    .stApp {
                    background: #0f172a !important;
                }

                    .block-container {
                        padding-left: 1rem !important;
                        padding-right: 1rem !important;
                    }

                    .stApp div[data-testid="stHorizontalBlock"] {
                        gap: 0.85rem;
                    }

                    .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) {
                        padding: 1rem !important;
                    }

                    .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) h2,
                    .stApp div[data-testid="stColumn"]:has(.workspace-card-marker) p {
                        color: #ffffff !important;
                    }
                }

        </style>
                """,unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp {
                    background:
                        linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.96)),
                        radial-gradient(circle at 15% 16%, rgba(192, 132, 252, 0.22), transparent 28%),
                        radial-gradient(circle at 88% 12%, rgba(34, 211, 238, 0.14), transparent 30%),
                        #0f172a !important;
                    color: #e2e8f0 !important;
                }

                @media (max-width: 760px) {
                    .stApp {
                        background: #0f172a !important;
                        color: #e2e8f0 !important;
                    }
                }

        </style>
                """,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
            /* Hide Top Bar of streamlit */
                #MainMenu, footer, header {
                    visibility: hidden;
                }

                .block-container {
                    padding-top: 1.5rem;
                    padding-bottom: 1.5rem;
                    max-width: 1180px;
                }

                h1 {
                    font-family: 'Outfit', sans-serif !important;
                    font-size: 3rem !important;
                    font-weight: 850 !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0.5rem !important;
                    
                }
                h2 {
                    font-family: 'Outfit', sans-serif !important;
                    font-size: 2rem !important;
                    font-weight: 800 !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0.5rem !important;
                }

                h3,h4,p{
                    font-family: 'Outfit', sans-serif ;

                }
                h1, h2, h3, h4, p, label, span {
                    color: #e2e8f0 !important;
                    overflow-wrap: anywhere;
                    word-break: normal;
                }
                div[data-testid="stAppViewContainer"] {
                    position: relative;
                }
                div[data-testid="stAppViewContainer"]:before {
                    content: "";
                    position: fixed;
                    inset: 0;
                    background:
                        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px),
                        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px);
                    background-size: 54px 54px;
                    mask-image: linear-gradient(to bottom, rgba(0,0,0,0.7), transparent 84%);
                    pointer-events: none;
                    z-index: 0;
                }
                .block-container {
                    position: relative;
                    z-index: 1;
                }
                div[data-testid="stMarkdownContainer"],
                div[data-testid="stText"],
                div[data-testid="stCaptionContainer"],
                div[data-testid="stAlert"] {
                    color: #e2e8f0 !important;
                }
                div[data-testid="stAlert"] {
                    background: rgba(15, 23, 42, 0.76) !important;
                    border: 1px solid rgba(148, 163, 184, 0.24) !important;
                    border-radius: 0.5rem !important;
                    box-shadow: 0 20px 45px -28px rgba(0,0,0,0.75) !important;
                }
                div[data-testid="stAlert"] p,
                div[data-testid="stAlert"] span,
                div[data-testid="stAlert"] div {
                    color: #e2e8f0 !important;
                    font-weight: 700 !important;
                }
                input,
                textarea,
                div[data-baseweb="select"] > div,
                div[data-baseweb="input"] > div,
                div[data-baseweb="textarea"] > div {
                    background: rgba(15, 23, 42, 0.72) !important;
                    color: #f8fafc !important;
                    border-color: rgba(255,255,255,0.16) !important;
                    border-radius: 0.5rem !important;
                }
                input::placeholder,
                textarea::placeholder {
                    color: #94a3b8 !important;
                }
                div[data-baseweb="select"] span,
                div[data-baseweb="select"] div {
                    color: #f8fafc !important;
                }
                div[data-testid="stDataFrame"],
                div[data-testid="stTable"] {
                    background: rgba(15, 23, 42, 0.72) !important;
                    border: 1px solid rgba(255,255,255,0.12) !important;
                    border-radius: 0.5rem !important;
                    color: #e2e8f0 !important;
                }
                div[data-testid="stCameraInput"],
                div[data-testid="stFileUploader"],
                div[data-testid="stForm"],
                div[data-testid="stVerticalBlockBorderWrapper"] {
                    background: rgba(15, 23, 42, 0.62) !important;
                    border: 1px solid rgba(255,255,255,0.12) !important;
                    border-radius: 0.5rem !important;
                    box-shadow: 0 20px 45px -26px rgba(0,0,0,0.65) !important;
                }
                div[data-testid="stCameraInput"] label,
                div[data-testid="stFileUploader"] label {
                    color: #f8fafc !important;
                    font-weight: 700 !important;
                }
                div[role="dialog"],
                div[data-testid="stDialog"] {
                    background:
                        linear-gradient(145deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.96)) !important;
                    border: 1px solid rgba(148, 163, 184, 0.24) !important;
                    border-radius: 0.5rem !important;
                    color: #e2e8f0 !important;
                    box-shadow: 0 28px 70px -28px rgba(0, 0, 0, 0.78) !important;
                }
                div[role="dialog"] h1,
                div[role="dialog"] h2,
                div[role="dialog"] h3,
                div[role="dialog"] p,
                div[role="dialog"] label,
                div[role="dialog"] span,
                div[role="dialog"] small,
                div[data-testid="stDialog"] h1,
                div[data-testid="stDialog"] h2,
                div[data-testid="stDialog"] h3,
                div[data-testid="stDialog"] p,
                div[data-testid="stDialog"] label,
                div[data-testid="stDialog"] span,
                div[data-testid="stDialog"] small {
                    color: #e2e8f0 !important;
                }
                div[role="dialog"] pre,
                div[role="dialog"] code,
                div[data-testid="stDialog"] pre,
                div[data-testid="stDialog"] code {
                    background: rgba(2, 6, 23, 0.72) !important;
                    border: 1px solid rgba(148, 163, 184, 0.18) !important;
                    border-radius: 0.5rem !important;
                    color: #f8fafc !important;
                }
                div[role="dialog"] div[data-testid="stAlert"],
                div[data-testid="stDialog"] div[data-testid="stAlert"] {
                    background: rgba(15, 23, 42, 0.82) !important;
                    border-color: rgba(34, 211, 238, 0.24) !important;
                    box-shadow: none !important;
                }
                div[role="dialog"] div[data-testid="stAlert"] *,
                div[data-testid="stDialog"] div[data-testid="stAlert"] * {
                    color: #e2e8f0 !important;
                }
                div[role="dialog"] button span,
                div[role="dialog"] button p,
                div[data-testid="stDialog"] button span,
                div[data-testid="stDialog"] button p {
                    color: #ffffff !important;
                }
                .dialog-panel {
                    background:
                        linear-gradient(145deg, rgba(30, 41, 59, 0.76), rgba(15, 23, 42, 0.82));
                    border: 1px solid rgba(148, 163, 184, 0.18);
                    border-radius: 0.5rem;
                    margin-bottom: 1rem;
                    padding: 1rem;
                }
                .dialog-panel h3 {
                    color: #f8fafc !important;
                    font-size: 1.2rem !important;
                    margin: 0 0 0.35rem !important;
                }
                .dialog-panel p {
                    color: #cbd5e1 !important;
                    line-height: 1.55 !important;
                    margin: 0 !important;
                }
                .dialog-kicker {
                    color: #67e8f9 !important;
                    font-size: 0.78rem !important;
                    font-weight: 850;
                    text-transform: uppercase;
                }
                button {
                    border-radius: 0.5rem !important;
                    background: linear-gradient(135deg, #0891b2, #059669) !important;
                    color: white !important;
                    padding: 11px 20px !important;
                    border: none !important;
                    font-weight: 750 !important;
                    min-height: 2.85rem !important;
                    white-space: normal !important;
                    transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                    }
                button div,
                button p,
                button span {
                    white-space: normal !important;
                    line-height: 1.25 !important;
                }
                button[kind="secondary"] {
                    border-radius: 0.5rem !important;
                    background-color: #334155 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                    }
                button[kind="primary"] {
                    background: linear-gradient(135deg, #0891b2, #059669) !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                    }
                button[kind="tertiary"] {
                    border-radius: 0.5rem !important;
                    background-color: rgba(30, 41, 59, 0.82) !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: 1px solid rgba(255,255,255,0.12) !important;
                    transition: transform 0.25s ease-in-out !important;
                    }
                button:hover {
                    transform: translateY(-1px) !important;
                    box-shadow: 0 16px 30px rgba(8, 145, 178, 0.24) !important;
                }
                .ai-hero {
                    background:
                        linear-gradient(145deg, rgba(30, 41, 59, 0.78), rgba(15, 23, 42, 0.76)),
                        radial-gradient(circle at 18% 18%, rgba(34, 211, 238, 0.15), transparent 34%);
                    border: 1px solid rgba(255,255,255,0.12);
                    border-radius: 0.5rem;
                    padding: 1.9rem;
                    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.55);
                    margin-bottom: 1.4rem;
                    position: relative;
                    overflow: hidden;
                    backdrop-filter: blur(18px);
                }
                .ai-hero:before {
                    content: "";
                    position: absolute;
                    inset: 0;
                    background:
                        linear-gradient(90deg, transparent, rgba(34,211,238,0.11), transparent),
                        repeating-linear-gradient(45deg, rgba(255,255,255,0.05) 0 1px, transparent 1px 11px);
                    pointer-events: none;
                }
                .ai-hero:after {
                    content: "";
                    position: absolute;
                    right: -70px;
                    top: -90px;
                    width: 210px;
                    height: 210px;
                    border-radius: 999px;
                    background: radial-gradient(circle, rgba(245,158,11,0.18), transparent 68%);
                    pointer-events: none;
                }
                .ai-eyebrow {
                    color: #67e8f9;
                    font-size: 0.85rem;
                    font-weight: 800;
                    text-transform: uppercase;
                    letter-spacing: 0 !important;
                }
                .ai-hero h1, .ai-hero h2 {
                    color: #f8fafc !important;
                    margin: 0.2rem 0 0.55rem !important;
                    position: relative;
                }
                .ai-hero p {
                    color: #cbd5e1;
                    margin: 0;
                    max-width: 760px;
                    position: relative;
                }
                .ai-section-title {
                    color: #f8fafc;
                    font-weight: 850;
                    font-size: 1.05rem;
                    margin: 0.6rem 0 0.7rem;
                }
                .ai-metric-card,
                .ai-feature-card {
                    background:
                        linear-gradient(145deg, rgba(30, 41, 59, 0.72), rgba(15, 23, 42, 0.76)),
                        radial-gradient(circle at 12% 10%, rgba(34,211,238,0.13), transparent 30%);
                    border: 1px solid rgba(255,255,255,0.12);
                    border-radius: 0.5rem;
                    padding: 1.25rem;
                    box-shadow: 0 25px 50px -24px rgba(0, 0, 0, 0.68);
                    margin-bottom: 0.75rem;
                    backdrop-filter: blur(16px);
                    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
                    position: relative;
                    overflow: hidden;
                    min-height: 128px;
                }
                .ai-metric-card:before,
                .ai-feature-card:before {
                    content: "";
                    position: absolute;
                    inset: 0 0 auto 0;
                    height: 3px;
                    background: linear-gradient(90deg, #22d3ee, #f59e0b, #10b981);
                    opacity: 0.9;
                }
                .ai-metric-card:hover,
                .ai-feature-card:hover {
                    transform: translateY(-2px);
                    border-color: rgba(34,211,238,0.35);
                    box-shadow: 0 28px 60px -26px rgba(8,145,178,0.48);
                }
                .ai-metric-card span,
                .ai-metric-card small,
                .ai-feature-card p {
                    color: #cbd5e1 !important;
                    display: block;
                    line-height: 1.55;
                }
                .ai-metric-card strong {
                    color: #67e8f9 !important;
                    display: block;
                    font-size: 2.15rem;
                    line-height: 1.1;
                    margin: 0.35rem 0;
                }
                .ai-feature-card strong {
                    color: #f8fafc !important;
                    display: block;
                    margin-bottom: 0.25rem;
                    font-size: 1.1rem;
                    line-height: 1.3;
                }
                .ai-feature-label {
                    color: #67e8f9 !important;
                    font-size: 0.92rem;
                    font-weight: 850;
                    text-transform: uppercase;
                    margin-bottom: 0.45rem;
                }
                .app-footer {
                    margin-top: 2rem;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #94a3b8 !important;
                    font-weight: 700;
                    letter-spacing: 0 !important;
                }
                .app-footer p {
                    color: #94a3b8 !important;
                    margin: 0;
                }
                .tab-grid-marker,
                .action-grid-marker,
                .workspace-card-marker {
                    display: none;
                }
                div[data-testid="stHorizontalBlock"]:has(.tab-grid-marker),
                div[data-testid="stHorizontalBlock"]:has(.action-grid-marker) {
                    align-items: stretch;
                }
                div[data-testid="stHorizontalBlock"]:has(.tab-grid-marker) button,
                div[data-testid="stHorizontalBlock"]:has(.action-grid-marker) button {
                    width: 100% !important;
                }
                .subject-card {
                    background:
                        linear-gradient(145deg, rgba(30,41,59,0.78), rgba(15,23,42,0.82)),
                        radial-gradient(circle at 12% 10%, rgba(34,211,238,0.15), transparent 34%);
                    border: 1px solid rgba(255,255,255,0.12);
                    border-radius: 0.5rem;
                    box-shadow: 0 25px 50px -24px rgba(0,0,0,0.68);
                    margin-bottom: 1.25rem;
                    overflow: hidden;
                    padding: 1.35rem;
                    position: relative;
                    min-height: 100%;
                }
                .subject-card-topline {
                    background: linear-gradient(90deg, #22d3ee, #f59e0b, #10b981);
                    height: 4px;
                    inset: 0 0 auto 0;
                    position: absolute;
                }
                .subject-card h3 {
                    color: #f8fafc !important;
                    font-size: 1.45rem !important;
                    margin: 0 0 0.75rem !important;
                    line-height: 1.25 !important;
                }
                .subject-meta {
                    color: #cbd5e1 !important;
                    font-size: 1rem;
                    line-height: 1.6;
                    margin: 0 0 1rem !important;
                }
                .subject-meta span {
                    background: rgba(34,211,238,0.16);
                    border: 1px solid rgba(34,211,238,0.24);
                    border-radius: 0.5rem;
                    color: #ecfeff !important;
                    display: inline-block;
                    font-weight: 800;
                    padding: 0.15rem 0.55rem;
                }
                .subject-stats {
                    display: grid;
                    gap: 0.7rem;
                    grid-template-columns: repeat(auto-fit, minmax(116px, 1fr));
                    margin-bottom: 1rem;
                }
                .subject-stat {
                    align-content: start;
                    background: rgba(148,163,184,0.14);
                    border: 1px solid rgba(255,255,255,0.08);
                    border-radius: 0.5rem;
                    color: #e2e8f0 !important;
                    display: grid;
                    gap: 0.22rem;
                    line-height: 1.35;
                    padding: 0.7rem 0.75rem;
                    min-width: 0;
                }
                .subject-stat .subject-stat-label {
                    color: #67e8f9 !important;
                    display: block;
                    font-size: 0.75rem !important;
                    font-weight: 850;
                    line-height: 1.1 !important;
                    margin-bottom: 0.25rem;
                    text-transform: uppercase;
                }
                .subject-stat strong {
                    color: #f8fafc !important;
                    display: block;
                    font-size: 1.12rem;
                    line-height: 1.15;
                }
                .subject-stat small {
                    color: #cbd5e1 !important;
                    display: block;
                    font-size: 0.82rem;
                    font-weight: 700;
                    line-height: 1.3;
                }
                .attendance-progress {
                    margin-top: 0.5rem;
                }
                .attendance-progress-label {
                    align-items: center;
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 0.45rem;
                }
                .attendance-progress-label span {
                    color: #cbd5e1 !important;
                    font-size: 0.9rem !important;
                    font-weight: 700;
                }
                .attendance-progress-label b {
                    color: #f8fafc !important;
                    font-size: 1rem;
                }
                .attendance-progress-track {
                    background: rgba(148,163,184,0.18);
                    border-radius: 999px;
                    height: 0.72rem;
                    overflow: hidden;
                }
                .attendance-progress-fill {
                    background: linear-gradient(90deg, #0891b2, #f59e0b, #10b981);
                    border-radius: 999px;
                    height: 100%;
                    min-width: 0.35rem;
                }
                .subject-overall-card {
                    margin-bottom: 1.25rem;
                    padding: 1.35rem !important;
                }
                .subject-overall-card h2 {
                    color: #67e8f9 !important;
                    font-size: 2.6rem !important;
                }
                @media (max-width: 760px) {

                    .block-container {
                        padding-left: 1rem !important;
                        padding-right: 1rem !important;
                    }

                    h1 {
                        font-size: 2rem !important;
                        line-height: 1.15 !important;
                    }

                    h2 {
                        font-size: 1.6rem !important;
                        line-height: 1.2 !important;
                    }

                    h3 {
                        font-size: 1.25rem !important;
                        line-height: 1.3 !important;
                    }

                    p,
                    label,
                    span {
                        font-size: 1rem !important;
                        line-height: 1.6 !important;
                    }

                    .subject-stats {
                        grid-template-columns: 1fr;
                    }
                    .subject-card {
                        padding: 1.1rem;
                    }
                    .subject-card h3 {
                        font-size: 1.25rem !important;
                    }
                    .subject-meta {
                        font-size: 0.95rem !important;
                    }
                    .subject-overall-card h2 {
                        font-size: 2.1rem !important;
                    }

                    div[data-testid="stHorizontalBlock"]:has(.tab-grid-marker),
                    div[data-testid="stHorizontalBlock"]:has(.action-grid-marker) {
                        display: grid !important;
                        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
                        gap: 0.75rem !important;
                    }

                    div[data-testid="stHorizontalBlock"]:has(.tab-grid-marker) > div,
                    div[data-testid="stHorizontalBlock"]:has(.action-grid-marker) > div {
                        width: 100% !important;
                        min-width: 0 !important;
                    }

                    button,
                    button[data-testid^="stBaseButton"] {
                        width: 100% !important;
                        min-height: 3rem !important;
                        padding: 0.85rem 1rem !important;
                        font-size: 0.95rem !important;
                        text-align: center !important;
                    }

                    button *,
                    button[data-testid^="stBaseButton"] * {
                        white-space: normal !important;
                    }

                    div[data-testid="stCameraInput"] img,
                    div[data-testid="stCameraInput"] video {
                        width: 100% !important;
                        height: auto !important;
                        object-fit: contain !important;
                        border-radius: 0.5rem !important;
                    }

                    div[data-testid="stDataFrame"] {
                        overflow-x: auto !important;
                    }

                    table {
                        min-width: 600px !important;
                    }

                    h1,
                    h2,
                    h3,
                    p,
                    span,
                    label {
                        overflow-wrap: break-word !important;
                        word-break: break-word !important;
                    }
                }

                @media (max-width: 520px) {
                    div[data-testid="stHorizontalBlock"]:has(.tab-grid-marker),
                    div[data-testid="stHorizontalBlock"]:has(.action-grid-marker) {
                        grid-template-columns: 1fr !important;
                    }
                }
        </style>
                """,unsafe_allow_html=True)
