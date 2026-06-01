'''Assignment Name : Spam Classifier Thinking
Description : Design a spam detection system: features, data needed, possible mistakes.'''




# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Step 1: Create dataset (you can also load CSV)
data = {
    "message": [
        "Win a free iPhone now",
        "Limited offer click now",
        "Meeting at 5 PM",
        "Call me later",
        "Congratulations you won a lottery",
        "Let's study together",
        "Free entry in contest",
        "Project submission tomorrow"
    ],
    "label": [
        "spam", "spam", "ham", "ham",
        "spam", "ham", "spam", "ham"
    ]
}

df = pd.DataFrame(data)

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.25, random_state=42
)

# Step 3: Convert text to numbers
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 4: Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 5: Test model
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 6: Predict new message
new_msg = ["You have won a free ticket"]
new_msg_vec = vectorizer.transform(new_msg)

prediction = model.predict(new_msg_vec)
user_input = input("Enter a message: ")

user_vec = vectorizer.transform([user_input])
print("Prediction:", model.predict(user_vec)[0])

