import streamlit as st
from pipelines.data_processing import preprocess_data
from pipelines.ml_models import run_model

def show_analysis():
    st.header("Data Analysis & ML Pipeline")
    uploaded = st.file_uploader("Upload FASTQ or CSV", type=["fastq","csv"])
    if uploaded:
        filter_threshold = st.slider('Quality threshold', 0.0, 1.0, 0.5)
        model_type = st.selectbox('Model type', ['RandomForest','SVM','XGBoost'])

        df = preprocess_data(uploaded, threshold=filter_threshold)
        st.subheader("Preprocessed Data")
        st.dataframe(df.head())

        metrics = run_model(df, model_type=model_type)
        st.subheader("Model Metrics")
        st.json(metrics)