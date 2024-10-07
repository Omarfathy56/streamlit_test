import pandas
import pandas as pd
import numpy as np
import streamlit as st
import plotly as px


@st.cache_data
def load_data():
    df = pandas.read_csv("imdb_top_1000.csv")
    df.columns = df.columns.str.lower()
    df.drop(["certificate"], axis=1, inplace=True)
    return df


st.title("IMDB Movies")

df = load_data()
st.write(df)
print(df.info())
print(df.isnull().mean()*100)
