import pickle
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def serialize_model():
    model = LogisticRegression(random_state=42)
    word_converter = CountVectorizer()

    data = [" ".join(list(movie_reviews.words(fileids=[f]))) for f in movie_reviews.fileids('neg')] + \
           [" ".join(list(movie_reviews.words(fileids=[f]))) for f in movie_reviews.fileids('pos')]

    word_converter.fit(data)

    x_train = word_converter.transform(data)
    y_train = [0] * 1000 + [1] * 1000

    model.fit(x_train, y_train)

    with open("LogReg.pkl", "wb") as file:
        pickle.dump(model, file)
    print("model trained and serialized!")

    with open("CountVect.pkl", "wb") as file:
        pickle.dump(word_converter, file)
    print("word_converter trained and serialized!")
