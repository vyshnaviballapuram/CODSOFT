# AI Movie Recommendation System

An AI-powered Movie Recommendation System built using **Machine Learning and Streamlit**.  
The application recommends movies based on user preferences using **Content-Based Filtering**.

---

## Features

**Smart Movie Recommendations**
- Suggests similar movies based on user-selected movie
- Uses Machine Learning algorithms for recommendations

**Genre Filtering**
- Filter recommendations based on movie genres

**Movie Search Suggestions**
- Search movies easily with dropdown suggestions

**Explainable AI**
- Shows why a movie is recommended
- Displays similarity percentage

**Similarity Score**
- Shows how closely movies match user interests

**Interactive UI**
- Built with Streamlit
- Clean and user-friendly interface

---

## Machine Learning Approach

This project uses:

### Content-Based Filtering

The system recommends movies by comparing movie features.

### Techniques Used:

- **TF-IDF Vectorization**
  - Converts movie information into numerical vectors

- **Cosine Similarity**
  - Calculates similarity between movies

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## Project Structure
Movie-Recommendation-System/

│
├── app.py
├── recommender.py
├── movies.csv
├── requirements.txt
└── README.md