import streamlit as st
import pickle
import pandas as pd
import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Define the file path (adjust as necessary)
file_path = 'C:/Users/Heckerbella/PycharmProjects/Recommender_system/deployment/movies_dict.pkl'

# Load the data
if os.path.exists(file_path):
    movies_dict = pickle.load(open(file_path, 'rb'))
else:
    st.error("The file 'movies_dict.pkl' was not found.")
    movies_dict = {}  # Or handle the missing file case appropriately

movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('C:/Users/Heckerbella/PycharmProjects/Recommender_system/deployment/similarity.pkl', 'rb'))

def recommender(movie):
    index = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    # top five similar movies

    recommended_movies = [] 
    for i in dist[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit application code
st.title('Movie Recommender System')
option = st.selectbox('Choose your movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommender(option)
    for i in recommendations:
        st.write(i)

