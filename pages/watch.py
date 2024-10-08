import streamlit as st
import main

st.title("watch")

df = main.load_data()

st.sidebar.markdown("my linked in account : [www.linkedin.com/in/omar-fathy-170865325]("
                    "https://www.linkedin.com/public-profile/settings?trk"
                    "=d_flagship3_profile_self_view_public_profile)")

movies_list = []

df['genre'] = df["genre"].str.split(",")
# put every genre in a list
list_genre = []
for rows in df['genre']:
    for nums in rows:
        if nums not in list_genre:
            list_genre.append(nums)
# show all movies or by genre
genre1 = st.radio("you want specific genre or not : ", [None, "yes"])
if genre1:
    genre1 = st.selectbox("choose specific genre if u want : ", list_genre)
if genre1 is None:
    for movie in df["series_title"]:
        movies_list.append(movie)
else:
    num1 = 0
    for genre2 in df['genre'].values:
        if genre1 in genre2:
            movie = df["series_title"][num1]
            movies_list.append(movie)
        num1 += 1

movie_name = st.selectbox("choose the movie you want : ", movies_list)


with st.container():
    col1, col2 = st.columns(2)
    with col2:
        if movie_name:
            director = df[df['series_title'] == movie_name]["director"]
            star1 = df[df['series_title'] == movie_name]["star1"]
            star2 = df[df['series_title'] == movie_name]["star2"]
            star3 = df[df['series_title'] == movie_name]["star3"]
            star4 = df[df['series_title'] == movie_name]["star4"]

            num = star1.index[0]
            st.subheader("Stars : ")
            st.markdown(f"🌟{star1[num]}🌟{star2[num]}🌟{star3[num]}🌟{star4[num]}")
    with col1:
        st.subheader("Overview : ")
        st.markdown(df['overview'][num])
st.subheader(f"Director : 🌟{director[num]}")



