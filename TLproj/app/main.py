import streamlit as st
from tabs.analysis_tab import show_analysis
from tabs.visualization_tab import show_visualization
from tabs.about_tab import show_about

st.set_page_config(page_title="Molecular Bio Pipeline", layout='wide')

tabs = {
    "Analysis": show_analysis,
    "Visualization": show_visualization,
    "About Team": show_about
}
choice = st.sidebar.radio("Tab Select", list(tabs.keys()))

tabs[choice]()