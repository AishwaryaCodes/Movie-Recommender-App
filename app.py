import pickle
import streamlit as st 
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1f1f09434d7147b5c6197ab22e53a1d9".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    
    return full_path
    
    
def recommend(movies, movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True , key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header("Movie Recommender App")
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Enter Movie Name',
    movie_list
)

if st.button('Get Recommendations'):
    recommended_movies_name, recommended_movies_poster = recommend(movies, selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    # Define a function to create HTML with wrapped text
    def create_html(name):
        return f"""
        <div style="width: 150px; height: 100px; overflow: hidden; text-overflow: ellipsis; white-space: normal;">
            {name}
        </div>
        """
        
        
    with col1:
        st.image(recommended_movies_poster[0])
        st.markdown(recommended_movies_name[0], unsafe_allow_html=True)
    
    with col2:
        st.image(recommended_movies_poster[1])
        st.markdown(recommended_movies_name[1], unsafe_allow_html=True)
        
    with col3:
        st.image(recommended_movies_poster[2])
        st.markdown(recommended_movies_name[2], unsafe_allow_html=True)
    
    with col4:
        st.image(recommended_movies_poster[3]) 
        st.markdown(recommended_movies_name[3], unsafe_allow_html=True) 
    
    with col5:
        st.image(recommended_movies_poster[4])     
        st.markdown(recommended_movies_name[4], unsafe_allow_html=True)