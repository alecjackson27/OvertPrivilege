from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from os import path
import pickle

from email_spam_detection import process_text


df = pd.read_csv('emails.csv')
df.drop_duplicates(inplace = True)

#Convert string to integer counts, learn the vocabulary dictionary and return term-document matrix
messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['text'])

print(df)
print(df['spam'])

"""
#Split the data into 80% training (X_train & y_train) and 20% testing (X_test & y_test) data sets
X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['spam'], test_size = 0.20, random_state = 0)
train_test_split()
"""