from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="短剧孵化器",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_PATH = Path(__file__).parent / "index.html"


def load_html() -> str:
    return HTML_PATH.read_text(encoding="utf-8")


st.title("短剧孵化器")
st.caption("Streamlit 部署入口。当前先承载现有 HTML 原型，后续可逐步迁移为原生 Streamlit 页面。")

components.html(load_html(), height=1600, scrolling=True)

