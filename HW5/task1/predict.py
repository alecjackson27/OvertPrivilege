import nltk
import sys
import pickle
from os import listdir
from sklearn.feature_extraction.text import CountVectorizer
from test import process_text, identity


def score_text(email):
    score = 0
    for classifier in listdir("classifiers"):
        with open("classifiers" + "/" + classifier, 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(email)
        score += prediction[0]
    return score


if __name__ == '__main__':
    email = [input("Enter the email: ")]
    #doc = CountVectorizer(analyzer=process_text).fit_transform(email)
    score = 0
    for classifier in listdir("classifiers"):
        with open("classifiers" + "/" + classifier, 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(email)
        score += prediction[0]
    print(score)
