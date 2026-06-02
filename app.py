import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Page layout styling
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# Download NLTK data quietly inside the Streamlit cache framework
@st.cache_resource
def load_nlp_resources():
    nltk.download('stopwords', quiet=True)
    return set(stopwords.words('english'))

stop_words = load_nlp_resources()

# Load dataset and train the model (Cached so it only runs once upon app startup)
@st.cache_resource
def train_model():
    # Dataset URL
    url = "https://raw.githubusercontent.com/lutzhamel/fake-news/master/data/fake_or_real_news.csv"
    df = pd.read_csv(url)
    
    # Text cleaning helper logic
    def clean_text(text):
        if not isinstance(text, str):
            return ""
        text = re.sub(r'[^\w\s]', '', text).lower()
        return ' '.join([word for word in text.split() if word not in stop_words])
        
    df['clean_text'] = df['text'].apply(clean_text)
    
    # Dataset splitting
    X_train, X_test, y_train, y_test = train_test_split(
        df['clean_text'], df['label'], test_size=0.2, random_state=42
    )
    
    # Vectorization & Fast Passive Aggressive Training
    tfidf = TfidfVectorizer(max_df=0.7)
    X_train_tfidf = tfidf.fit_transform(X_train)
    
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(X_train_tfidf, y_train)
    
    return tfidf, pac, clean_text

# Instantiate the built model assets
tfidf, pac, clean_text = train_model()

# --- STREAMLIT UI ---
st.title("📰 Fake News Detector")
st.markdown("This mini-app utilizes **TF-IDF Feature Extraction** paired with a **Passive Aggressive Classifier** trained natively via `scikit-learn` to analyze the factual integrity of political text strings.")

st.subheader("Analyze News Content")
user_input = st.text_area("Paste the text block of a news article below:", height=250, placeholder="Insert content here...")

if st.button("Evaluate Text", type="primary"):
    if not user_input.strip():
        st.warning("Please input valid text content to begin analysis.")
    else:
        with st.spinner("Analyzing linguistic features..."):
            # Process & predict
            processed_input = clean_text(user_input)
            vector_input = tfidf.transform([processed_input])
            prediction = pac.predict(vector_input)[0]
            
            st.write("---")
            if prediction == "REAL":
                st.success("### ✅ Prediction: This content maps closely to factual **REAL** news indicators.")
            else:
                st.error("### 🚨 Prediction: This content maps closely to fabricated **FAKE** news indicators.")
