# ======== recommender.py ========

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, interactions_path):
        """
        interactions_path: string — path to CSV file containing user-item interaction data.
        The CSV is expected to have at least these columns:
            user_id, item_id, rating  (or some numeric feedback / implicit feedback)
        """
        self.df = pd.read_csv(r"C:\Users\HP\Downloads\Movie.csv")
        self.user_item = None
        self.item_similarity = None

    def preprocess(self):
        """
        Convert raw interaction DataFrame into user-item matrix.
        Rows: user_id, Columns: item_id, Values: rating (or 0 if no interaction).
        """
        self.user_item = self.df.pivot(
            index='userId', columns='movie', values='rating'
        ).fillna(0)

    def build_item_similarity(self):
        """
        Compute item-item similarity matrix using cosine similarity.
        The matrix will have item_ids as both rows and columns.
        """
        # Transpose user_item matrix: now rows = items, columns = users
        item_user_matrix = self.user_item.T

        # Compute cosine similarity between all pairs of items
        sim_matrix = cosine_similarity(item_user_matrix)

        # Build DataFrame for easy lookup
        self.item_similarity = pd.DataFrame(
            sim_matrix,
            index=self.user_item.columns,
            columns=self.user_item.columns
        )

    def recommend(self, user_id, top_n=5):
        """
        Given a user_id, recommend top_n items the user has not interacted with yet.
        Returns a list of item_ids.
        """
        if user_id not in self.user_item.index:
            print(f"[WARN] user_id {user_id} not found in data.")
            return []

        # User's ratings vector
        user_ratings = self.user_item.loc[user_id]

        # Items the user has not rated / interacted with (assumed rating == 0)
        items_not_rated = user_ratings[user_ratings == 0].index

        # Compute a recommendation score for each candidate item
        scores = {}
        for item in items_not_rated:
            # similarity vector: how similar this item is to all items
            sim_scores = self.item_similarity[item]
            # score = dot product of user's ratings & similarity — higher means more likely
            score = np.dot(user_ratings, sim_scores)
            scores[item] = score

        # Sort items by score (descending) and return top_n
        recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        return [item for item, _ in recommended]


if __name__ == "__main__":
    # Example usage (for testing)
    rec = Recommender("data/interactions.csv")
    rec.preprocess()
    rec.build_item_similarity()

    test_user = input("Enter user_id: ")
    try:
        test_user = int(test_user)
    except:
        pass

    recs = rec.recommend(user_id=test_user, top_n=5)
    print("Recommended items:", recs)
