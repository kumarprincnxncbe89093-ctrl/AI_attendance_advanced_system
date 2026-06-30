import streamlit as st

import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name,subject_code):
    app_domain="prince8564.streamlit.app"
    join_url=f"{app_domain}/?join-code={subject_code}"

    st.markdown(
        f"""
        <div class="dialog-panel">
            <div class="dialog-kicker">Subject sharing</div>
            <h3>{subject_name}</h3>
            <p>Share the enrollment link or let students scan the QR code to join this class.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    qr=segno.make(join_url)

    out=io.BytesIO()

    qr.save(out,kind='png',scale=10,border=1)

    col1,col2=st.columns(2)

    with col1:
        st.markdown("#### Enrollment Link")
        st.code(join_url,language="text")
        st.markdown("#### Subject Code")
        st.code(subject_code,language="text")
        st.info("Share the link through WhatsApp, email, or your class group.")


    with col2:
        st.markdown("#### QR Scan")
        st.image(out.getvalue(),caption="Scan to join")

