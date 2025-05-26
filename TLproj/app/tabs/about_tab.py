import streamlit as st

def show_about():
    st.header("Ομάδα Ανάπτυξης")
    st.markdown("Η εργασία μπορεί να γίνει ατομικά ή σε ομάδα 2-3 ατόμων.")
    members = {
        'Μέλος Α': 'Data processing & UI',
        'Μέλος Β': 'ML models & Docker',
        'Μέλος Γ': 'Visualization & Documentation'
    }
    for name, contrib in members.items():
        st.markdown(f"**{name}**: {contrib}")