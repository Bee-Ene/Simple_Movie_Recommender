import streamlit as st
import pickle
import pandas as pd
import os

print("Current Working Directory:", os.getcwd())

file_path = 'C:/file_path/movies_dict.pkl'

# Loading data
if os.path.exists(file_path):
    movies_dict = pickle.load(open(file_path, 'rb'))
else:
    st.error("The file 'movies_dict.pkl' was not found.")
    movies_dict = {}  

movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('C:/file_path/similarity.pkl', 'rb'))

def recommender(movie):
    index = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    # top 5 similar movies

    recommended_movies = [] 
    for i in dist[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit
st.title('Movie Recommender System')
option = st.selectbox('Choose your movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommender(option)
    for i in recommendations:
        st.write(i)

