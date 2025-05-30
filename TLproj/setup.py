from setuptools import setup, find_packages

setup(
    name="molbio_app",
    version="0.1",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        "streamlit>=1.0",
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "biopython",
        "xgboost"
    ],
)
