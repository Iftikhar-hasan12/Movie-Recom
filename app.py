import pickle
import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        return None

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        st.error(f"Error in recommendation: {str(e)}")
        return [], []

# Main app
st.header('🎬 Movie Recommender System')

# Load data with error handling
try:
    movies = pickle.load(open('model/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("❌ Model files not found. Please make sure 'movie_list.pkl' and 'similarity.pkl' are in the 'model' folder.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model files: {str(e)}")
    st.stop()

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    help="Choose a movie you like to get similar recommendations"
)

if st.button('Show Recommendations', type='primary'):
    if selected_movie:
        with st.spinner('Finding similar movies...'):
            recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        
        if recommended_movie_names:
            
            
            # Create columns for recommendations (updated from beta_columns)
            cols = st.columns(5)
            
            for i in range(len(cols)):
                with cols[i]:
                    if i < len(recommended_movie_names):
                        #st.text(recommended_movie_names[i])
                        if recommended_movie_posters[i]:
                             st.image(recommended_movie_posters[i], use_container_width=True)
                        else:
                            st.warning("Poster not available")
        else:
            st.warning("No recommendations found. Please try another movie.")
    else:
        st.warning("Please select a movie first!")

