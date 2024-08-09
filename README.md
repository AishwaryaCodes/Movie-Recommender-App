Movies Recommender App

A simple Movie Recommender application built using Python, Streamlit, and The Movie Database (TMDB) API. The app recommends movies based on a selected movie and displays posters of the recommended movies.

## Features

- **Movie Recommendations**: Get personalized movie recommendations based on the selected movie.
- **Movie Posters**: View posters of the recommended movies for a more visual experience.

## Tech Stack

- **Python**: The core programming language used for the logic and functionality.
- **Streamlit**: Used for building the interactive web application.
- **TMDB API**: Utilized to fetch movie details and posters.
- **Jupyter Notebook**: Used for data exploration, preprocessing, and model development.

## API Key
The app uses TMDB API to fetch movie posters. Make sure to use your own TMDB API key in the fetch_poster function.

## Project Structure

- `main.py`: Contains the main logic for the application, including functions for fetching posters and recommending movies.
- `artifacts/`: Directory containing pre-processed data such as `movie_list.pkl` and `similarity.pkl` used for recommendations.

## Usage
Select a movie from the dropdown menu.
Click on "Get Recommendations" to view a list of recommended movies along with their posters.


 **Clone the repository**:
   ```bash
   git clone https://github.com/AishwaryaCodes/Movie-Recommender-App.git


## Run Project
Command: streamlit run app.py