import streamlit as st
import pickle
import pandas as pd
import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

file_path = 'pkl_file_path'

# Load the data
if os.path.exists(file_path):
    movies_dict = pickle.load(open(file_path, 'rb'))
else:
    st.error("The file 'movies_dict.pkl' was not found.")
    movies_dict = {}  #handle missing error file more properly

movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('pkl_file_path', 'rb'))

def recommender(movie):
    index = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    #recommend top five similar movies

    recommended_movies = [] 
    for i in dist[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit application 
st.title('Movie Recommender System')
option = st.selectbox('Choose your movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommender(option)
    for i in recommendations:
        st.write(i)

