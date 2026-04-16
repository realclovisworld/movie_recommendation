#load necessary libraries
import streamlit as st
import pandas as pd
import requests
import pickle
from dotenv import load_dotenv
import os

load_dotenv() #loads variables form .env

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # top 5
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Fetch movie poster from TMDB API (cached)
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    api_key = os.getenv("tmdb_api_key")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except requests.RequestException:
        return None
    return None

# Streamlit UI
st.title("🎬 SYNAPSE MOVIE RECOMMENDATION SYSTEM")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_movie)
    st.subheader("Your top 5 Movie Suggestions: ")

    # Create columns dynamically (only for the actual recommendations)
    cols = st.columns(len(recommendations))
    for col, (_, row) in zip(cols, recommendations.iterrows()):
        poster_url = fetch_poster(row["movie_id"])
        with col:
            if poster_url:
                st.image(poster_url, width=130)
            st.caption(row["title"])
