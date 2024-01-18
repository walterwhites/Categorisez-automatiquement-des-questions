import nltk
import re
from bs4 import BeautifulSoup
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    text = lowercase_text(text)
    text = remove_urls(text)
    # Tokenization
    word_tokens = tokenization(text)
    word_tokens = clear_ponctuation(word_tokens)
    # custom clean
    word_tokens = custom_clean(word_tokens)
    # Lemmatisation
    lemmatized_words = lemmatization(word_tokens)
    # Suppression des stopwords
    return remove_stopwords(lemmatized_words)

def remove_urls(text):
    regex = r'https?://\S+|www\.\S+'
    text = re.sub(regex, '', text)
    return text

def custom_clean(text):
    # remplacer les sauts de lignes par des espaces
    word_tokens = [word_token.replace('\n', ' ') for word_token in text]
    # supprimer les espaces en trop
    word_tokens = [re.sub(r'\s+', ' ', phrase) for phrase in word_tokens]
    return word_tokens

def lowercase_text(text):
    return text.lower()

def tokenization(text):
    return sent_tokenize(text)

def lemmatization(word_tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in word_tokens]

def lemmatize_and_flatten(phrases):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for phrase in phrases for word in ' '.join(phrase).split()]

def remove_stopwords(sentences):
    stop_words = set(stopwords.words('english'))
    result = []
    for sentence in sentences:
        words = sentence.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        result.append(' '.join(filtered_words))
    return result

def clear_ponctuation(text):
    return [re.sub(r'[^a-zA-Z0-9\s]', '', phrase) for phrase in text]

def extract_text_from_body(html_body):
    soup = BeautifulSoup(html_body, 'html.parser')
    return soup.get_text()