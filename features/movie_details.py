import streamlit as st
import requests

def show_movie_details(movie_id, fetch_movie_details):
    st.markdown("---")
    st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        st.session_state.current_view = "home"
        st.session_state.selected_movie_details = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    movie_data = fetch_movie_details(movie_id)
    if movie_data:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            poster_path = movie_data.get('poster_path')
            if poster_path:
                st.image(f"https://image.tmdb.org/t/p/w500/{poster_path}", use_column_width=True)
        
        with col2:
            st.markdown(f"<h1 style='color: #e50914;'>{movie_data.get('title', 'N/A')}</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 16px; color: #ccc;'>{movie_data.get('tagline', '')}</p>", unsafe_allow_html=True)
            
            # Movie metadata
            col2_1, col2_2, col2_3 = st.columns(3)
            with col2_1:
                st.metric("Rating", f"⭐ {movie_data.get('vote_average', 'N/A')}")
            with col2_2:
                st.metric("Runtime", f"⏱️ {movie_data.get('runtime', 'N/A')} min")
            with col2_3:
                st.metric("Release Date", movie_data.get('release_date', 'N/A'))
            
            # Genres
            genres = [genre['name'] for genre in movie_data.get('genres', [])]
            st.markdown(f"**Genres:** {', '.join(genres)}")
            
            # Overview
            st.markdown("### Overview")
            st.markdown(f"<p style='color: #ccc; line-height: 1.6;'>{movie_data.get('overview', 'No overview available.')}</p>", unsafe_allow_html=True)
            
            # Watch button
            if st.button("▶️ Watch Now", type="primary", use_container_width=True):
                st.success("🎬 Starting playback... (This is a demo)")