Movie Recommendation System
Overview

This project is a content-based movie recommendation system that suggests similar movies based on textual metadata such as overview, genres, keywords, cast, and crew information. The system uses vectorization techniques and cosine similarity to measure the closeness between movies. A Streamlit-based user interface is provided to allow users to interact with the recommender system.

Features

Processes TMDB movie and credits datasets.

Cleans and extracts meaningful metadata from JSON-formatted text fields.

Generates a "tags" column combining overview, genres, keywords, cast, and crew.

Vectorizes text data using CountVectorizer.

Computes cosine similarity among all movies.

Recommends five similar movies based on the selected movie.

Displays movie posters using The Movie Database (TMDB) API.

Offers an interactive interface built using Streamlit.

Dataset

The project uses the following datasets:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Both datasets are available publicly on Kaggle.

Project Structure
.
├── model/
│   ├── movie_list.pkl
│   ├── similarity.pkl
├── app.py
├── notebook.ipynb
├── requirements.txt
└── README.md


movie_list.pkl
Contains the processed movie dataframe used by the recommender.

similarity.pkl
Contains the cosine similarity matrix used to compute recommendations.
