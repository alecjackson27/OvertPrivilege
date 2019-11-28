'''
Citations:
Code from the article (1) and associated github account (2) below used as a starting point:
1. https://medium.com/@randerson112358/email-spam-detection-using-python-machine-learning-abe38c889855
2. https://github.com/randerson112358/Python/blob/master/Email_Spam_Detection/Email_Spam_Detection.ipynb

emails.csv data set from: https://www.kaggle.com/balakishan77/spam-or-ham-email-classification/data
'''


import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import LinearSVC


#Tokenization (a list of tokens), will be used as the analyzer
#1.Punctuations are [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
#2.Stop words in natural language processing, are useless words (data).
def process_text(text):
    '''
    What will be covered:
    1. Remove punctuation
    2. Remove stopwords
    3. Return list of clean text words
    '''
    
    #1
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    #2
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    
    #3
    return clean_words

if __name__ == "__main__":
    df = pd.read_csv('emails.csv')


    #Check for and remove duplicates
    df.drop_duplicates(inplace = True)

    #Convert string to integer counts, learn the vocabulary dictionary and return term-document matrix
    messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['text'])


    #Split the data into 80% training (X_train & y_train) and 20% testing (X_test & y_test) data sets
    X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['spam'], test_size = 0.20, random_state = 0)


    #Create and train the Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

    print("NB")
    print()

    #Print the predictions
    print(classifier.predict(X_train))

    #Print the actual values
    print(y_train.values)

    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Print the predictions
    print('Predicted value: ',classifier.predict(X_test))

    #Print Actual Label
    print('Actual value: ',y_test.values)

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))


    #Create and train the LinearSVC classifier
    classifier = LinearSVC(max_iter=10_000)
    classifier.fit(X_train, y_train)

    print("SVC")
    print()

    #Print the predictions
    print(classifier.predict(X_train))

    #Print the actual values
    print(y_train.values)

    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Print the predictions
    print('Predicted value: ',classifier.predict(X_test))

    #Print Actual Label
    print('Actual value: ',y_test.values)

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))


    #Create and train the SGDClassifier
    classifier = SGDClassifier()
    classifier.fit(X_train, y_train)

    print("SGD")
    print()

    #Print the predictions
    print(classifier.predict(X_train))

    #Print the actual values
    print(y_train.values)

    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Print the predictions
    print('Predicted value: ',classifier.predict(X_test))

    #Print Actual Label
    print('Actual value: ',y_test.values)

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))
