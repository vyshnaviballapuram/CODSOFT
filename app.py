import streamlit as st
from recommender import MovieRecommender
genres_list = [
    "All",
    "Action",
    "Adventure",
    "Comedy",
    "Drama",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "Crime",
    "Animation"
]

st.set_page_config(
page_title="Movie AI",
layout="wide"
)


st.title("AI Movie Recommendation System")


model=MovieRecommender()
st.sidebar.title("Movie AI")

st.sidebar.markdown(
"""
### About Project

This AI Movie Recommendation System
uses Machine Learning to suggest movies
based on your interests.

**Tech Used:**
- Python
- Pandas
- Scikit-learn
- Streamlit

**ML Technique:**
Content Based Filtering

Uses:
TF-IDF + Cosine Similarity
"""
)


st.sidebar.divider()


selected_genre = st.sidebar.selectbox(
    "Select Genre",
    genres_list
)

movie = st.selectbox(
    "Search your movie",
    [""] + list(model.movies["title"].head(1000))
)


if st.button("Recommend"):

    results = model.recommend(movie)
    if selected_genre != "All":

        results = [
            r for r in results
            if selected_genre.lower()
            in r["genres"].lower()
        ]

    if results:

        cols=st.columns(5)


        for i,m in enumerate(results):

            with cols[i]:

                import os


                

                st.subheader(m["title"])

                st.write(
                "Match:",
                m["score"],
                "%"
                )

                st.caption(
                m["overview"]
                )

                st.success(
                m["reason"]
                )


    else:
        st.error("Movie not found!!")