from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import string
from nltk.corpus import stopwords

import pickle


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

def identity(words):
    return words

def create_pipeline(estimator):
    steps = [
        ('vectorize', CountVectorizer(
            analyzer=process_text, tokenizer=identity,
            preprocessor=None, lowercase=False
        )),
    ]

    # Add the estimator
    steps.append(('classifier', estimator))
    return Pipeline(steps)


if __name__ == "__main__":
    df = pd.read_csv('emails.csv')
    df.drop_duplicates(inplace = True)

    #Convert string to integer counts, learn the vocabulary dictionary and return term-document matrix
    #messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['text'])

    #print(messages_bow)
    #print(df['spam'])

    model_num = 1

    for classifier in (MultinomialNB(), LinearSVC(max_iter=10_000), SGDClassifier()):
        model = create_pipeline(classifier)
        model.fit(df['text'], df['spam'])

        model_path = "classifier-" + str(model_num)
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        model_num += 1
