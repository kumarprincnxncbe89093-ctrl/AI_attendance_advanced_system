import streamlit as st
from html import escape


def _metric_card(label, value, helper):
    st.markdown(
        f"""
        <div class="ai-metric-card">
            <span>{escape(str(label))}</span>
            <strong>{escape(str(value))}</strong>
            <small>{escape(str(helper))}</small>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_grid(metrics):
    cols = st.columns(len(metrics), gap="medium")
    for col, metric in zip(cols, metrics):
        with col:
            _metric_card(*metric)


def render_feature_card(title, body, icon):
    st.markdown(
        f"""
        <div class="ai-feature-card">
            <div class="ai-feature-label">{escape(str(icon))}</div>
            <strong>{escape(str(title))}</strong>
            <p>{escape(str(body))}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
