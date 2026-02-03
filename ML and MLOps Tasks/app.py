import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

@st.cache_resource
def load_resources():
    # Loading the model and the vectorizer
    with open('sentiment_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
        
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    
    return model, vectorizer

model, tfidf = load_resources()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    clean_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(clean_words)

# Interface
st.title("Flipkart Review Sentiment Analyzer")
st.write("Enter a product review to classify it as **Positive** or **Negative**.")
user_input = st.text_area("Enter Review Text Here:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip():
        cleaned_text = preprocess_text(user_input)
        vectorized_text = tfidf.transform([cleaned_text])
        
        prediction = model.predict(vectorized_text)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        # Display Result
        if sentiment == "Positive":
            st.success(f"**Sentiment: {sentiment}** 😄")
        else:
            st.error(f"**Sentiment: {sentiment}** 😞")
    else:
        st.warning("Please enter some text first.")