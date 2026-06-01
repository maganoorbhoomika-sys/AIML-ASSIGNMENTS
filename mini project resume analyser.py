import nltk
from nltk.corpus import stopwords
from nltk.tokenise  import word_tokenise
import string

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    #lowercase
    text=text.lower();
    #tokenize
    words=words_tokenize(text)
    #remove stopwords and punctuations
    stop_words=set(stopwords.words('english'))

    filterd_words=[
        word for word in words
        if word nt in stop_words and word not in string.punctuation
        ]