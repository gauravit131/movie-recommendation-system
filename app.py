from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the movie data and similarity matrix
try:
    with open('movie_dict.pkl', 'rb') as f:
        movies_dict = pickle.load(f)
        movies = pd.DataFrame(movies_dict)
    with open('similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    print("Error: Make sure 'movie_dict.pkl' and 'similarity.pkl' are in the same directory.")
    # Handle the error gracefully, maybe exit or provide a default response
    movies = pd.DataFrame()
    similarity = None

@app.route('/')
def home():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Returns movie recommendations based on user input.
    Expects a JSON payload with a 'movie' key.
    """
    if similarity is None:
        return jsonify({'error': 'Recommendation model not loaded.'}), 500

    data = request.get_json()
    movie_name = data.get('movie', '').strip()

    if not movie_name:
        return jsonify({'error': 'Movie name is required.'}), 400

    # Find the index of the movie
    try:
        movie_index = movies[movies['title'].str.lower() == movie_name.lower()].index[0]
    except IndexError:
        return jsonify({'error': f"Movie '{movie_name}' not found."}), 404

    # Get similarity scores and recommend movies
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return jsonify({'recommendations': recommended_movies})

@app.route('/movies', methods=['GET'])
def get_movie_titles():
    """Returns a list of all movie titles for autocomplete."""
    if not movies.empty:
        return jsonify({'titles': movies['title'].tolist()})
    return jsonify({'titles': []})


if __name__ == '__main__':
    app.run(debug=True)
