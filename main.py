import pandas
import pandas as pd
import numpy as np
import streamlit as st
import plotly as px


@st.cache_data
def load_data():
    df = pandas.read_csv("imdb_top_1000.csv")
    df.columns = df.columns.str.lower()
    df["poster"] = np.nan
    df['released_year'] = pd.to_datetime(df['released_year'], format='mixed', errors='coerce')
    df['year'] = df['released_year'].dt.year
    df.drop(["certificate", "poster_link", "released_year"], axis=1, inplace=True)
    return df


st.sidebar.markdown("my linked in account : [www.linkedin.com/in/omar-fathy-170865325]("
                    "https://www.linkedin.com/public-profile/settings?trk"
                    "=d_flagship3_profile_self_view_public_profile)")

st.title("IMDB Top 1000 Movies")

df = load_data()
st.write(df)

# creating a container with the logo of imdb and intro to the app

with st.container():
    col1, col2 = st.columns(2)
    with col2:
        st.image("imdb.jpg", width=200)
    with col1:
        st.markdown("<h1 style'text-align: left; color: red;'>Welcome to IMDB movies shower </h1>",
                    unsafe_allow_html=True)
