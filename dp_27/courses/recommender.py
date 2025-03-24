import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Course

def get_recommendations(user_disability):
    courses = Course.objects.all()
    data = pd.DataFrame(list(courses.values()))

    if data.empty:
        return []

    # Modify feature representation to focus on disability-related aspects
    data['features'] = data['category'] + " " + data.get('disability_support', "")

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data['features'])

    # Use only the user's disability for similarity matching
    user_input = user_disability
    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    data['score'] = similarity_scores

    recommended_courses = data.sort_values(by='score', ascending=False).head(4)

    return recommended_courses[['title', 'description', 'external_url', 'image_url']].to_dict(orient='records')
