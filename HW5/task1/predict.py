import nltk
import sys
import pickle
from os import listdir
from sklearn.feature_extraction.text import CountVectorizer
from test import process_text, identity
import re


def score_text(email):
    score = 0
    for classifier in listdir("classifiers"):
        with open("classifiers" + "/" + classifier, 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(email)
        score += prediction[0]
    return score


HTTP_PATTERN = r"(https?://[-.\w]+)"

def find_url(text):
    urls = re.compile(HTTP_PATTERN).findall(text)
    return urls


def suspicious_url(text):
    urls = find_url(text)
    for word in ('update', 'login', 'verify'):
        for url in urls:
            if word in url:
                return [1, -1]
    for url in urls:
        if url[0:12] == 'https://www.':
            if url[12].isdigit():
                return [1, 1]
        if url[0:13] == "https://www3.":
            if url[13].isdigit():
                return [1, 1]
        if url[0:8] == 'https://':
            if url[8].isdigit():
                return [1, 1]
        if url[0:7] == "http://":
            if url[7].isdigit():
                return [1, 1]
    return [0, 0]


if __name__ == '__main__':
    
    email = input("Enter the email: ")
    print(suspicious_url(email))
    """
    #doc = CountVectorizer(analyzer=process_text).fit_transform(email)
    score = 0
    for classifier in listdir("classifiers"):
        with open("classifiers" + "/" + classifier, 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(email)
        score += prediction[0]
    print(score)
    """
