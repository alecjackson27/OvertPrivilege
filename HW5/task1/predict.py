import nltk
import sys
import pickle
from os import listdir
from sklearn.feature_extraction.text import CountVectorizer
from test import process_text, identity


if __name__ == '__main__':
    email = [input("Enter the email: ")]
    #doc = CountVectorizer(analyzer=process_text).fit_transform(email)
    score = 0
    for classifier in listdir("classifiers"):
        with open("classifiers" + "/" + classifier, 'rb') as f:
            model = pickle.load(f)
        
        #with open(sys.argv[1], 'r') as f:
        #    doc = f.read()
        
        prediction = model.predict(email)
        score += prediction[0]
    print(score)
