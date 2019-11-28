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

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import LinearSVC
from operationalize import create_pipeline, identity, process_text


if __name__ == "__main__":
    df = pd.read_csv('emails.csv')


    #Check for and remove duplicates
    df.drop_duplicates(inplace = True)


    #Split the data into 80% training (X_train & y_train) and 20% testing (X_test & y_test) data sets
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['spam'], test_size = 0.20, random_state = 0)


    #Create and train the Naive Bayes classifier
    classifier = create_pipeline(MultinomialNB())
    classifier.fit(X_train, y_train)

    print("NB")
    print()

    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))


    #Create and train the LinearSVC classifier
    classifier = create_pipeline(LinearSVC(max_iter=10_000))
    classifier.fit(X_train, y_train)

    print("SVC")
    print()


    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))


    #Create and train the SGDClassifier
    classifier = create_pipeline(SGDClassifier())
    classifier.fit(X_train, y_train)

    print("SGD")
    print()

    #Evaluate the model on the training data set
    pred = classifier.predict(X_train)
    print(classification_report(y_train ,pred ))
    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
    print()
    print('Accuracy: ', accuracy_score(y_train,pred))

    #Evaluate the model on the test data set
    pred = classifier.predict(X_test)
    print(classification_report(y_test ,pred ))

    print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
    print()
    print('Accuracy: ', accuracy_score(y_test,pred))
