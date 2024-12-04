# recipe_recommendation_system
**Project Overview**
The Recipe Recommendation System is a web-based application that suggests recipes to users based on their input of ingredients. It leverages Word2Vec for natural language processing and cosine similarity for recommendation, providing personalized recipe suggestions.

**Features**
**User Input**: Users input available ingredients.
**Recipe Recommendation**: Provides top 5 recipe suggestions based on similarity to the user's input.
**Pretrained Word2Vec**: Enhances understanding of ingredient semantics.

**Interactive Interface**:
**Homepage**: Navigate the system.
**Login**: Placeholder for future user authentication.
**About**: Information about the application.
**JSON API**: Returns recommendations in JSON format for integration.

**Technology Stack**
Backend: Flask
Frontend: HTML, CSS, JavaScript (templates in Flask)
NLP Model: Word2Vec (Gensim)
Data Storage: Pandas DataFrame (cleaned recipe data)
Similarity Metric: Cosine Similarity
**Dependencies:**
Flask
numpy
pandas
gensim
nltk
scikit-learn

![Homepage](screenshots/Screenshot%2024-12-04%20141900.png)
![Recommendations](screenshots/Screenshot%2024-12-04%20141944.png)
![Login Page](screenshots/Screenshot%2024-12-04%20142020.png)
