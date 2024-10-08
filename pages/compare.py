import streamlit as st
import main
import plotly.express as px

df = main.load_data()

st.sidebar.markdown("my linked in account : [www.linkedin.com/in/omar-fathy-170865325]("
                    "https://www.linkedin.com/public-profile/settings?trk"
                    "=d_flagship3_profile_self_view_public_profile)")

df.drop(['poster', 'overview', ], axis=1, inplace=True)

st.subheader(" The TOP Page ")

num = st.number_input("choose the number of movies : ", 0, 1000)

st.title("compare")

st.write(f"Top {num} movies by rating")

df.sort_values('imdb_rating', inplace=True, ascending=False)

data = df.nlargest(num, columns='imdb_rating')

st.plotly_chart(px.bar(data, x='series_title', y="imdb_rating", color="series_title"))


st.write(f"Top {num} movies by meta score")

df.sort_values('meta_score', inplace=True, ascending=False)

data1 = df.nlargest(num, columns='meta_score')

st.plotly_chart(px.bar(data1, x='series_title', y="meta_score", color="series_title"))


st.write(f"Top {num} movies by number of votes")

df.sort_values('no_of_votes', inplace=True, ascending=False)

data1 = df.nlargest(num, columns='no_of_votes')

st.plotly_chart(px.bar(data1, x='series_title', y="no_of_votes", color="series_title"))