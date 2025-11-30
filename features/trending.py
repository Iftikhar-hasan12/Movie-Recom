import streamlit as st
import random

def show_trending_movies(movies, fetch_poster):
    st.markdown("<h1 style='color: #e50914;'>🔥 Trending Now</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        st.session_state.current_view = "home"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Get random trending movies (in real app, you'd have actual trending data)
    trending_movies = random.sample(list(movies.iterrows()), min(10, len(movies)))
    
    st.markdown("### Popular This Week")
    cols = st.columns(5)
    for idx, (_, movie) in enumerate(trending_movies[:5]):
        with cols[idx]:
            poster = fetch_poster(movie['movie_id'])
            if poster:
                st.image(poster, use_column_width=True)
            st.markdown(f"<p style='text-align: center;'><strong>{movie['title']}</strong></p>", unsafe_allow_html=True)
    
    st.markdown("### Top Picks for You")
    cols2 = st.columns(5)
    for idx, (_, movie) in enumerate(trending_movies[5:10]):
        with cols2[idx]:
            poster = fetch_poster(movie['movie_id'])
            if poster:
                st.image(poster, use_column_width=True)
            st.markdown(f"<p style='text-align: center;'><strong>{movie['title']}</strong></p>", unsafe_allow_html=True)