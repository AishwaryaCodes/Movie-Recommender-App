<div align="center" style="position: relative; width: 100%; max-width: 900px; margin: auto;">
  <!-- Full-width background image -->
  <img src="Movie Recommender.jpg" alt="Movie Recommender" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); filter: brightness(0.7);">

  <!-- Overlay text -->
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: #fff; font-family: Arial, sans-serif;">
    <h1 style="font-size: 3.5rem; margin: 0; font-weight: bold;">Movies Recommender App</h1>
    <p style="font-size: 1.5rem; margin-top: 10px; max-width: 800px; line-height: 1.6;">
      A smart app to help you find your next favorite movie. Powered by <b>Python</b>, <b>Streamlit</b>, and <b>TMDB API</b>.
    </p>
  </div>
</div>

---

# 🌟 **Overview**

The **Movies Recommender App** is an interactive web application designed to make movie discovery effortless and enjoyable. Leveraging a similarity-based recommendation algorithm and dynamic movie posters from TMDB, it offers users a personalized and visually appealing experience.

---

## 💡 **Problem Statement**

With endless movies across multiple platforms, finding the next best movie to watch can be overwhelming. Many solutions lack visual appeal or personalization, which leaves users unsatisfied.

---

## 🧩 **Solution**

1. **Tailored Recommendations:** Using similarity-based modeling, the app suggests movies that align with the selected title.
2. **Visual Interface:** Dynamic, high-quality movie posters ensure an engaging experience.
3. **Ease of Access:** Built with Streamlit, it's lightweight and user-friendly, even for non-technical users.

---

# 🚀 **Key Features**

- **Personalized Movie Recommendations:** Choose a movie, and the app generates suggestions based on its features.
- **Dynamic Posters:** Visualize recommended movies with posters fetched directly from TMDB.
- **Intuitive Interface:** A seamless user experience with a sleek design and easy navigation.

---

# 🛠️ **Tech Stack**

| Technology      | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| **Python**       | Backend logic and implementation of recommendation algorithms.         |
| **Streamlit**    | Simple, interactive web-based front-end development.                   |
| **TMDB API**     | Dynamic movie data and poster retrieval.                               |
| **Jupyter**      | Used for exploratory data analysis and model development.              |

---

# 📂 **Project Structure**

The project is organized as follows:

```plaintext
├── app.py            # Streamlit application entry point
├── artifacts/        # Preprocessed data for recommendations
├── requirements.txt  # List of required Python packages
├── README.md         # Project documentation
└── assets/           # Screenshots and visual assets
```

---

# 🖼️ **Screenshots and visual assets**
---

### **Homepage**

The app's main page, featuring the title, dropdown menu for movie selection, and the "Get Recommendations."
<div align="center">
  <img src="https://github.com/user-attachments/assets/5590ca4b-12d3-4829-af35-e7dc48fe6bc1" alt="Homepage Screenshot" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);">
</div>

---

### **Recommendation Results**

Displays a curated list of recommended movies names/Keywords.
<div align="center">
  <img src="https://github.com/user-attachments/assets/3a6531c7-6972-457a-861c-94ebdb94faa4" alt="Recommendations Screenshot" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);">
</div>

---

### **Visual Results** 

Showcases the posters of all recommended movies for an enhanced user experience.
<div align="center">
  <img src="https://github.com/user-attachments/assets/29a3ad27-702b-4831-aeab-21f6a67c5429" alt="Results Screenshot" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);">
</div>

---

# 🛠️ **How It Works**

1. **Select a Movie:** Choose from a dropdown menu.
2. **Get Recommendations:** Hit "Get Recommendations" to generate results.
3. **View Results:** The app displays similar movies with their posters.

---

# 🔮 **Future Enhancements**

- **Advanced Models:** Introduce collaborative filtering or neural networks for improved recommendations.
- **User Accounts:** Enable users to save recommendations and create watchlists.
- **Global Reach:** Add support for regional and international movies in multiple languages.

---

# 🔧 **Setup Instructions**

1. **Clone the Repository:**
   

   git clone https://github.com/AishwaryaCodes/Movie-Recommender-App.git



2. **Install Dependencies:**
   

   pip install -r requirements.txt


3. **Add TMDB API Key:**
   Replace the placeholder in the fetch_poster function with your TMDB API Key. You can generate your API key from the TMDB API website.


4. **Run the Application:**
   

   streamlit run app.py



5. **Access the App:**
   Open the URL provided by Streamlit (e.g., http://localhost:8501) in your browser to interact with the app.

<br> 
<br>


## **Enjoying Perfect Movie Picks App**
<div align="center">
  <img src="users.jpg" alt="Users enjoying movie" width="700">
</div>

<div align="center" style="font-size: 18px; color: #555; margin-top: 30px;"> Thank you for exploring the Movies Recommender App.</div>
