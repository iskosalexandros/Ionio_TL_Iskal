import streamlit as st


def show_about():
    st.header("Η Εργασία έγινε από τον")
    members = {
        'Ίσκο Αλέξανδρο': 'Π2020198'
    }
    for name, contrib in members.items():
        st.markdown(f"**{name}**: {contrib}")