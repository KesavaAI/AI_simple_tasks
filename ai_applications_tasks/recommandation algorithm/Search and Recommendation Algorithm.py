
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# Sample shopping data
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
    'product_name': ['laptop', 'phone', 'printer', 'phone', 'monitor', 'laptop', 'mouse', 'keyboard']
}
df = pd.DataFrame(data)
# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
# Compute TF-IDF matrix for product_name column
tfidf_matrix = tfidf_vectorizer.fit_transform(df['product_name'])

# Calculate cosine similarity between products
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# Function to get product recommendations for a given product
def get_recommendations(product_name):
    idx = df[df['product_name'] == product_name].index[0]  # Get the index of the product
    sim_scores = list(enumerate(cosine_sim[idx]))  # Get similarity scores for all products
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Sort products by similarity
    sim_scores = sim_scores[1:11]  # Get top 10 similar products (excluding itself)
    product_indices = [score[0] for score in sim_scores]  # Get the indices of top similar products
    recommended_products = df['product_name'].iloc[product_indices]  # Get the product names from indices
    return recommended_products
# Example usage:
user_interests = ['laptop', 'phone']
recommended_products = set()
for interest in user_interests:
    recommendations = get_recommendations(interest)
    recommended_products.update(recommendations)
print("Recommended products based on user interests:")
print(recommended_products)
