# ======== app.py ========

import streamlit as st
from recommender import Recommender

# Path to your interaction dataset
DATA_PATH = "data/interactions.csv"

@st.cache_data   # (optional) caches results so you don't recompute on every run
def load_recommender():
    rec = Recommender(DATA_PATH)
    rec.preprocess()
    rec.build_item_similarity()
    return rec

def main():
    st.title("🛠️ Simple Recommendation System")

    rec = load_recommender()

    user_input = st.text_input("Enter user_id:")
    n = st.number_input("How many recommendations?", min_value=1, value=5)

    if st.button("Recommend"):
        if user_input.strip() == "":
            st.write("Please enter a valid user_id.")
        else:
            try:
                user_id = int(user_input)
            except:
                st.write("Invalid user_id format — should be integer (or adjust according to your data).")
                return

            recs = rec.recommend(user_id=user_id, top_n=n)
            if not recs:
                st.write("No recommendations found (user not found or no candidate items).")
            else:
                st.write("Recommended item IDs:", recs)

if __name__ == "__main__":
    main()
