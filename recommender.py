import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:

    def __init__(self):

        self.movies = pd.read_csv("movies.csv")


        self.movies["overview"] = (
            self.movies["overview"]
            .fillna("")
        )


        self.movies["genres"] = (
            self.movies["genres"]
            .fillna("")
        )


        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )


        self.matrix = self.vectorizer.fit_transform(
            self.movies["genres"]
            +
            self.movies["overview"]
        )


        self.similarity = cosine_similarity(
            self.matrix
        )


    def recommend(self, movie):

        movie = movie.lower()


        matches = self.movies[
            self.movies["title"]
            .str.lower()
            .str.contains(movie)
        ]


        if matches.empty:
            return []


        index = matches.index[0]


        scores = list(
            enumerate(
                self.similarity[index]
            )
        )


        scores = sorted(
            scores,
            key=lambda x:x[1],
            reverse=True
        )


        result=[]


        for i,score in scores[1:6]:

            movie_data = self.movies.iloc[i]


            result.append(
                {
                "title": movie_data["title"],
                "overview": movie_data["overview"],
                "genres": movie_data["genres"],
                "score": round(score*100,2),

                "reason":
                f"Recommended because it has similar genres and storyline "
                f"({round(score*100,2)}% similarity)"
                }
            )


        return result