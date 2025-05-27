import streamlit as st
from tabs.about_tab import show_about
from tabs.analysis_tab import show_analysis
from tabs.visualization_tab import show_visualization

st.set_page_config(page_title="Molecular Bio Pipeline", layout='wide')

tabs = {
    "Analysis": show_analysis,
    "Visualization": show_visualization,
    "About Me": show_about
}
choice = st.sidebar.radio("Tab Select", list(tabs.keys()))

tabs[choice]()