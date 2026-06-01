'''Build a Text Cleaner
Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.'''

import string

# Sample stopwords list (you can expand this)
stopwords = {
    'the', 'is', 'in', 'and', 'to', 'of', 'a', 'for', 'on', 'with', 
    'as', 'by', 'an', 'at', 'from'
}

def clean_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    
    # Join back to sentence
    cleaned_text = " ".join(filtered_words)
    
    return cleaned_text


# 🔹 Test the function
sample_text = "Hello!!! This is a simple example, showing how TEXT cleaning works in Python."

cleaned = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned)