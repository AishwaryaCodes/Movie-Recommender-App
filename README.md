**Movies Recommender App**

The Movies Recommender App is an intuitive and interactive web application I developed, designed to recommend movies based on a selected title. Leveraging the power of Python, Streamlit, and the TMDB API, this application enhances user experience by providing visually appealing recommendations through movie posters. The project showcases my ability to integrate APIs, preprocess data, and create user-friendly interfaces.
<br>
<br>

**Problem Statement:**
With the overwhelming number of movies available across streaming platforms, users often face difficulty in choosing what to watch next. Traditional methods of searching for recommendations can be time-consuming and do not provide a visually engaging experience.
<br>
<br>

**Challenge:**
Users wanted a quick, personalized, and visually appealing way to explore similar movies based on their preferences.
<br>
<br>
<br>
**Solution**

The Movies Recommender App solves this problem by providing:
   1) Personalized Recommendations: Using a similarity-based recommendation model, the app suggests movies that align with the user's choice.
   2) Visual Experience: It fetches and displays posters of recommended movies, offering users a richer browsing experience.
   3) Ease of Use: Built on Streamlit, the app is simple, intuitive, and accessible, catering to users of all technical backgrounds.
<br>

**Features**

- Get personalized movie recommendations based on the selected movie.
- Visual Movie Posters: Displays high-quality posters of recommended movies for an engaging experience.
<br>
  
**Tech Stack**

   1) Python - Implemented the core logic and backend functionality.
   2) Streamlit - Built an interactive, user-friendly front-end interface.
   3) TMDB API - Integrated to fetch movie details and high-quality posters dynamically.
   4) Jupyter Notebook - Utilized for data preprocessing, exploration, and model development.
<br>

**Project Structure**

   - main.py: Contains the main application logic, including functions for fetching movie posters and generating recommendations.
   - artifacts/: Stores pre-processed files (movie_list.pkl and similarity.pkl) used to calculate movie similarities and provide recommendations.
<br>

**How It Works**

   1) Select a Movie: Choose a movie from the dropdown menu in the app.
   2) Get Recommendations: Click on the "Get Recommendations" button.
   3) View Results: The app displays a list of similar movies along with their posters for a visually engaging experience.
<br>

**Screenshot**

Screenshot 1: <br>
Homepage: The app's main page, featuring the title, dropdown menu for movie selection, and the "Get Recommendations"
<img src="https://github.com/user-attachments/assets/5590ca4b-12d3-4829-af35-e7dc48fe6bc1" alt="image" width="700" height="500">
<br>

Screenshot 2: <br>
Recommendation Dropdown: Displays a curated list of recommended movies.
<img src="https://github.com/user-attachments/assets/3a6531c7-6972-457a-861c-94ebdb94faa4" alt="image" width="700" height="500">

<br>

Screenshot 3: <br>
Visual Results: Showcases the posters of all recommended movies for an enhanced user experience.
<img src="https://github.com/user-attachments/assets/29a3ad27-702b-4831-aeab-21f6a67c5429" alt="image" width="700" height="500">


**Future Scope**

The Movies Recommender App has significant potential for further enhancements:
   1) User Login and Watchlist: Add user authentication and allow users to save recommended movies to a personal watchlist.
   2) Recommendation Algorithms: Upgrade the recommendation engine to include collaborative filtering or deep learning-based models for improved accuracy.
   3) Multilingual Support: Add support for movie recommendations and posters in multiple languages to cater to a global audience.

<br>
<br>

**Setup Instructions**

Clone the Repository: git clone https://github.com/AishwaryaCodes/Movie-Recommender-App.git

Install Dependencies: pip install -r requirements.txt

Add TMDB API Key: Replace the placeholder in the fetch_poster function with your TMDB API Key. You can generate your API key from the TMDB API website.

Run the Application: streamlit run app.py

Access the App: Open the URL provided by Streamlit (e.g., http://localhost:8501) in your browser to interact with the app.


