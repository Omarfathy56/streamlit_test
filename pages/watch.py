import streamlit as st
import main


st.title("watch")

df = main.load_data()

movies_list = []
for movie in df["series_title"]:
    movies_list.append(movie)

movie_name = st.selectbox("choose the movie you want : ", movies_list)
if movie_name:
    st.image(df[df['series_title'] == movie_name]["poster_link"].values)

