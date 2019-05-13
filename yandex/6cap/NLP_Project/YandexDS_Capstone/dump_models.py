from nlp_process_data import text_cleaning
import pickle
import pandas as pd
import numpy as np

from nltk.stem.porter import PorterStemmer

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


def handle_rawdata(series, func=None):
    if not func:
        raise ValueError('no stemmer was passed into function')
    return text_cleaning(series, func)


def serialize_model():

    try:
        data = pd.read_csv('yandex_phone_reviews.csv', sep=',', )
    except ValueError:
        print("NO phone_reviews_final.csv FOUND")
        raise SystemExit

    X_train = handle_rawdata(data['rev'], PorterStemmer().stem)
    y_train = data['mark']

    model = LogisticRegression(C=0.1, class_weight={0: 3, 1: 1}, solver='lbfgs', n_jobs=-1)
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=3)

    vectorizer.fit(X_train)
    model.fit(vectorizer.transform(X_train), y_train)

    coef = model.coef_.tolist()[0]
    most_valuable_features = [coef.index(i) for i in sorted(coef)[:100]]
    features = np.array(vectorizer.get_feature_names())

    mvf = features[most_valuable_features]
    mvf_cnt = [vectorizer.vocabulary_.get(i) for i in mvf]

    most_valuable_words = sorted(list(zip(mvf, mvf_cnt)), key=lambda tup: tup[1])

    with open('model_stats.pkl', 'wb') as file:
        pickle.dump([mvf, most_valuable_words], file)
    print("model words statistics are serialized!")

    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
    print("model trained and serialized!")

    with open("vectorizer.pkl", "wb") as file:
        pickle.dump(vectorizer, file)
    print("word_converter trained and serialized!")
