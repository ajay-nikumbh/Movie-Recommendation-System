# Import the lib's
from select import select
import streamlit as st
import pickle 
import pandas as pd
import requests

# Load the pickle file
movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity=   pickle.load(open('sim.pkl','rb'))


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
     'How would you like to be contacted?',movies['title'].values)


# Fetch poster function
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a3aedb5e9e320d15c8eafd901e79e008&language=en-US'.format(movie_id))

    data = response.json()
    
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
 
# Recommed function
def rc(movie):
    
    # Fetch the index
    movie_index= movies[movies['title'] == movie].index[0]
    
    # Fetch the distances
    distances = similarity[movie_index]
    
    # Get the 5 similar movies 
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    # Now print the first indexe's of the top 5 similar movies
    recommend_movies =[]
    recommend_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters

        

if st.button('Recommend'):
    names, posters= rc(selected_movie_name)
    
    col1, col2, col3 ,col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
