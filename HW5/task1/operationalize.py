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

#print(messages_bow)
#print(df['spam'])

model_num = 1

for model in (MultinomialNB(), LinearSVC(max_iter=10_000), SGDClassifier()):
    model = MultinomialNB()
    model.fit(messages_bow, df['spam'])

    model_path = "classifier-" + str(model_num)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    model_num += 1
