import streamlit as st
from html import escape

def subject_card(name,code,section,stats=None,footer_callback=None,progress_percent=None,progress_label=None):
    safe_name = escape(str(name))
    safe_code = escape(str(code))
    safe_section = escape(str(section))
    safe_progress_label = escape(str(progress_label or "Attendance"))
    progress_value = 0

    if progress_percent is not None:
        try:
            progress_value = max(0, min(100, int(round(float(progress_percent)))))
        except (TypeError, ValueError):
            progress_value = 0

    html=f"""
        <div class="subject-card" style="background:linear-gradient(145deg, rgba(30,41,59,0.78), rgba(15,23,42,0.82)); border:1px solid rgba(255,255,255,0.12); border-radius:8px; box-shadow:0 25px 50px -24px rgba(0,0,0,0.68); margin-bottom:20px; overflow:hidden; padding:22px; position:relative;">
        <div class="subject-card-topline" style="background:linear-gradient(90deg,#22d3ee,#f59e0b,#10b981); height:4px; left:0; position:absolute; right:0; top:0;"></div>
        <h3 style="color:#f8fafc !important; font-size:1.45rem; line-height:1.25; margin:0 0 12px;">{safe_name}</h3>
        <p class="subject-meta" style="color:#cbd5e1 !important; line-height:1.6; margin:0 0 16px;">Code : <span style="background:rgba(34,211,238,0.16); border:1px solid rgba(34,211,238,0.24); border-radius:8px; color:#ecfeff !important; display:inline-block; font-weight:800; padding:2px 9px;">{safe_code}</span> | Section : {safe_section}</p>
        """
    if stats:
        html+='<div class="subject-stats" style="display:grid; gap:11px; grid-template-columns:repeat(3,minmax(0,1fr)); margin-bottom:16px;">'

        for icon,label,value in stats:
            html+=(
                '<div class="subject-stat" style="background:rgba(148,163,184,0.14); border:1px solid rgba(255,255,255,0.08); border-radius:8px; color:#e2e8f0 !important; line-height:1.35; min-width:0; padding:11px 12px;">'
                f'<span class="subject-stat-label" style="color:#67e8f9 !important; display:block; font-size:0.75rem; font-weight:850; line-height:1.1; margin-bottom:4px; text-transform:uppercase;">{escape(str(icon))}</span>'
                f'<strong style="color:#f8fafc !important; display:block; font-size:1.28rem; line-height:1.2;">{escape(str(value))}</strong>'
                f'<small style="color:#cbd5e1 !important; display:block; font-size:0.86rem; margin-top:2px;">{escape(str(label))}</small>'
                '</div>'
            )

        html+="</div>"

    if progress_percent is not None:
        html+=f"""
        <div class="attendance-progress" style="margin-top:8px;">
            <div class="attendance-progress-label" style="align-items:center; display:flex; justify-content:space-between; margin-bottom:7px;">
                <span style="color:#cbd5e1 !important; font-size:0.9rem; font-weight:700;">{safe_progress_label}</span>
                <b style="color:#f8fafc !important;">{progress_value}%</b>
            </div>
            <div class="attendance-progress-track" style="background:rgba(148,163,184,0.18); border-radius:999px; height:12px; overflow:hidden;">
                <div class="attendance-progress-fill" style="background:linear-gradient(90deg,#0891b2,#f59e0b,#10b981); border-radius:999px; height:100%; min-width:6px; width:{progress_value}%"></div>
            </div>
        </div>
        """

    html+="</div>"

    st.markdown(html,unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
