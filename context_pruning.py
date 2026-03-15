from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prune_context(question, documents):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([question] + documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    top_index = similarity.argmax()

    return documents[top_index]