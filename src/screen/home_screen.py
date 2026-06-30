import streamlit as st
from src.components.header import header_home
from src.components.erp_widgets import render_feature_card
from src.ui.base_layout import style_base_layout, style_background_home
from pathlib import Path
from src.components.footer import footer_home
BASE_DIR = Path.cwd()   # Project root


def home_screen():
    student_logo = BASE_DIR / "student.png"
    teacher_logo = BASE_DIR / "teacher.png"

    header_home()
    style_background_home()
    style_base_layout()
    col1,col2 =st.columns(2,gap="large")
    with col1:
        st.markdown('<span class="workspace-card-marker"></span>', unsafe_allow_html=True)
        st.header("Student Workspace")
        st.image(str(student_logo), width=96)
        render_feature_card(
            "Recognition Tools",
            "Face login, course enrollment, attendance tracking, and biometric profile update.",
            "Student",
        )
        if st.button("Open Student Workspace",type="primary",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"]="student"
            st.rerun()
    with col2:
        st.markdown('<span class="workspace-card-marker"></span>', unsafe_allow_html=True)
        st.header("Teacher Workspace")
        st.image(str(teacher_logo), width=96)
        render_feature_card(
            "Model Operations",
            "Subject creation, subject sharing, face attendance, voice attendance, and attendance records.",
            "Teacher",
        )
        if st.button("Open Teacher Workspace",type="primary",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"]="teacher"
            st.rerun()
    footer_home()
