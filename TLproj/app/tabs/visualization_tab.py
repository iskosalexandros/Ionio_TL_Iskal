import sys
import streamlit as st
from app.pipelines.utils import plot_pca, plot_heatmap


def show_visualization():
    st.header("Visualization")
    st.subheader("PCA Plot")
    st.pyplot(plot_pca())

    st.subheader("Expression Heatmap")
    st.pyplot(plot_heatmap())