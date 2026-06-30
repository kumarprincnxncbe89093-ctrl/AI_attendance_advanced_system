import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown(
        """
        <div class="dialog-panel">
            <div class="dialog-kicker">Subject setup</div>
            <h3>Create Subject</h3>
            <p>Add the subject code, name, and section for attendance tracking.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    sub_id=st.text_input("Subject Code",placeholder="E.g CUCS1004")
    sub_name=st.text_input("Subject Name",placeholder="Introduction to Computer Science")
    sub_section=st.text_input("Section",placeholder="A")

    if st.button("Create Subject Now",type="primary",width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject created successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error : {str(e)}")
        else:
            st.warning("Please fill all the fields")
