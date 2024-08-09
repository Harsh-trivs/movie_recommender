import streamlit.components.v1 as components
import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

# Dropdown menu
selected_movie = st.selectbox("Select a movie:", movies['title'])

# display matches


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = []
    for i in distance[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


recommendations = recommend(selected_movie)

st.write("Recommended movies:")
for i in recommendations:
    st.write(i)
