import streamlit as st
import pandas as pd

def show_search_feature(movies, fetch_poster, fetch_movie_details):
    st.markdown("<h1 style='color: #e50914;'>🔍 Search Movies</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        st.session_state.current_view = "home"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Search box
    search_query = st.text_input("Search for movies...", placeholder="Enter movie title")
    
    if search_query:
        # Simple search functionality
        search_results = movies[movies['title'].str.contains(search_query, case=False, na=False)]
        
        if not search_results.empty:
            st.markdown(f"### Found {len(search_results)} results for '{search_query}'")
            
            # Display results in grid
            cols_per_row = 4
            results_list = list(search_results.iterrows())
            
            for i in range(0, len(results_list), cols_per_row):
                cols = st.columns(cols_per_row)
                for j in range(cols_per_row):
                    if i + j < len(results_list):
                        idx, movie = results_list[i + j]
                        with cols[j]:
                            poster = fetch_poster(movie['movie_id'])
                            if poster:
                                st.image(poster, use_column_width=True)
                            st.markdown(f"<p style='text-align: center;'><strong>{movie['title']}</strong></p>", unsafe_allow_html=True)
                            
                            if st.button("View Details", key=f"search_{idx}", use_container_width=True):
                                st.session_state.selected_movie_details = movie['movie_id']
                                st.session_state.current_view = "details"
        else:
            st.warning("No movies found matching your search.")