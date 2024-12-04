from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import gensim
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import nltk

# Ensure you download required nltk data
nltk.download("punkt")

app = Flask(__name__)

# Load preprocessed recipe data and the Word2Vec model
df_clean = pd.read_csv('data/final_recipes.csv')  # Load your cleaned dataset
w2v_model = Word2Vec.load('models/word2vec_model.pkl')  # Load trained Word2Vec model

# Load all recipe vectors (precomputed)
all_recipes_vector = np.load('models/recipe_vectors.npy')

# Function to vectorize user input using Word2Vec model
def user_input_vectorize(user_input):
    user_input_tokens = word_tokenize(user_input)
    user_input_vector = [0] * w2v_model.vector_size
    num_tokens = 0

    for token in user_input_tokens:
        if token in w2v_model.wv:
            user_input_vector = [a + b for a, b in zip(user_input_vector, w2v_model.wv[token])]
            num_tokens += 1

    if num_tokens > 0:
        user_input_vector = [x / num_tokens for x in user_input_vector]

    return np.array(user_input_vector).reshape(1, -1)

# Function to recommend recipes
def recommend_w2v(user_input_vector):
    similarities = cosine_similarity(user_input_vector, all_recipes_vector)
    N = 5  # Top 5 recommendations
    top_indices = similarities.argsort()[0][-N:][::-1]  # Get top N indices
    return df_clean.loc[top_indices, ['title', 'items', 'instructions']]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        
        # Placeholder for real authentication
        if username == "admin" and password == "password":  # Example credentials
            return jsonify({"status": "success", "message": "Login successful!"})
        else:
            return jsonify({"status": "error", "message": "Invalid username or password."})

    return render_template('login.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['ingredients']  # Get user input from form
    user_input_vector = user_input_vectorize(user_input)
    recommendations = recommend_w2v(user_input_vector)

    # Convert recommendations to a list of dictionaries for easy display in HTML
    recommended_recipes = recommendations.to_dict(orient='records')
    return jsonify(recommended_recipes)

if __name__ == '__main__':
    app.run(debug=True)
