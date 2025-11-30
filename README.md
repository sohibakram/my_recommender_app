# Movie Recommender App

A **Streamlit-based movie recommender system** built with Python and pandas. This app allows users to get movie recommendations based on historical user ratings.

---

## Features

* User-friendly interface using Streamlit.
* Loads movie rating data from CSV.
* Provides personalized recommendations.
* Easy to run locally and deploy.

---

## Project Structure

```
my_recommender_project/
│
├── app.py             # Main Streamlit app
├── recommender.py     # Recommender class and preprocessing logic
├── Movie.csv          # Movie dataset (user ratings)
├── requirements.txt   # Python dependencies
└── venv/              # Virtual environment (ignored in Git)
```

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/username/my_recommender_app.git
cd my_recommender_app
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## Usage

* Select a user or movie from the sidebar.
* Click **Recommend**.
* View personalized movie recommendations.

---

## Dependencies

* Python 3.10+
* pandas
* numpy
* streamlit
* scikit-learn (if your recommender uses similarity models)

---

## Notes

* Ensure the CSV file (`Movie.csv`) is in the project root.
* Column names in the CSV should match the expected format: `user_id`, `movie_id`, `rating`.

---

## License

MIT License

---

## Author

Sohib Akram
Data Scientist | Python & Machine Learning Enthusiast
