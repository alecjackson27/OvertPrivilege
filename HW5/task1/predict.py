import nltk
import sys
import pickle
from os import listdir
from sklearn.feature_extraction.text import CountVectorizer
from email_spam_detection import process_text


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
        print(prediction[0])
    else:
        print('Please give only the path to the model and the document as arguments')