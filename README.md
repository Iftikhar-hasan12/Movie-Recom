# **Movie Recommendation System**

## **Overview**
**Movie Recommendation System** is a content-based recommendation engine that suggests movies similar to a selected title using textual metadata such as **overview**, **genres**, **keywords**, **cast**, and **crew**.

The system uses **CountVectorizer** to vectorize text data and **cosine similarity** to compute similarity between movies. Users interact with the system via a **Streamlit-based web interface**.

## **Features**

Processes and merges **TMDB movies** and **credits datasets**.

Extracts and cleans metadata from JSON-formatted fields.

Combines **overview**, **genres**, **keywords**, **cast**, and **crew** into a **tags column**.

Vectorizes movie tags using **CountVectorizer**.

Computes **cosine similarity** for movie recommendations.

Provides top 5 similar movie recommendations.

Displays movie posters using the **TMDB API**.

Interactive **Streamlit web interface** for easy usage.

## **Technology Stack**

**Backend & ML**

**Python 3.x**

**Pandas** — Data manipulation

**NumPy** — Numerical computations

**Scikit-learn** — CountVectorizer, cosine similarity

**Frontend**

**Streamlit** — Web interface

**Requests** — Fetch movie posters from TMDB API

## **Dataset**

**tmdb_5000_movies.csv** — Movie details

**tmdb_5000_credits.csv** — Cast & crew information

Both datasets are publicly available on **Kaggle**.

## **Project Structure**

movie-recommender/
├── model/
│   ├── movie_list.pkl           # Processed movie dataframe
│   ├── similarity.pkl           # Cosine similarity matrix
├── app.py                       # Streamlit application
├── notebook.ipynb               # Data preprocessing and feature building
├── requirements.txt             # Python dependencies
└── README.md


## **Installation**

**1. Clone the Repository**

git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system


**2. Create Virtual Environment (Optional)**

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate.bat     # Windows


**3. Install Dependencies**

pip install -r requirements.txt


## **Usage**

**Run the Streamlit app**

streamlit run app.py


Select a movie from the dropdown to view top 5 recommended movies along with their posters.

## **Model Details**

**Data Preprocessing**

Merge movies and credits datasets on **title**.

Extract top 3 cast members and director from JSON.

Combine **overview**, **genres**, **keywords**, **cast**, and **crew** into **tags column**.

**Vectorization**

Use **CountVectorizer** (max_features=5000, stop_words='english')

**Similarity Calculation**

Compute **cosine similarity** between vectorized tags.

**Pickle Files**

**movie_list.pkl** — stores processed movie dataframe

**similarity.pkl** — stores cosine similarity matrix

## **Deployment (Azure / Cloud)**

Push your project to GitHub.

Create an **Azure Web App** service.

Connect GitHub repository to Azure Web App.

Configure Startup Command (Linux):

streamlit run app.py --server.port 8000 --server.address 0.0.0.0


Deploy using Azure or GitHub Actions.

**Notes:** For large models (>100 MB), use **Git LFS** or **Azure Blob Storage**.
