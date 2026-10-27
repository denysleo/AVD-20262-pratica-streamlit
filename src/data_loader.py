import pandas as pd
import streamlit as st

# TODO: adicionar @st.cache_data (import streamlit as st) para evitar reler o CSV a cada interação
@st.cache_data
def load_data(path="data/clean/titanic_clean.csv"):
    """Lê o dataset já tratado (exportado ao final do notebook de EDA)."""
    return pd.read_csv(path)
