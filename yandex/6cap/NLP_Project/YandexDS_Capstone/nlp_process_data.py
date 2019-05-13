import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score


def build_pipe(vect, model, stopwords=None, ngram_range=(1, 1), min_df=3):
    return Pipeline([("count", vect(stop_words=stopwords, ngram_range=ngram_range, 
                                    min_df=min_df)),
                     ("model", model())])


def text_cleaning(data, func):
    # This func applies given func to every word
    # Regex capture only rus, lat words
    # Returns Series -> Series[row] = text:str
    series = data.copy()
    for i in range(data.shape[0]):
        text = series.iloc[i]
        pattern = re.compile(r"(?u)[a-zа-я]+")
        word_list = re.findall(pattern, text.lower())
        series.iloc[i] = " ".join([func(w) for w in word_list if len(w) > 2])
    return series


def handle_rawdata(X_train, X_test, func=None):
    # Appiles apply_to_str, text_cleaning functions to given Series
    pr_data = list()
    for data in [X_train, X_test]:
        pr_data.append(text_cleaning(data, func))
    return pr_data


def train_test_models(X_train, y_train, cv=3, models_cls=None, vectorizer_cls=None, 
                      random_state=None, min_df=None,stopwords=None, 
                      ngram_range=(1, 1), model_names=None, vectorizer_names=None):
    
    worked_models = list()
    mean = list()
    scores = list()
    
    if not models_cls or not vectorizer_names:
        models_cls = [LogisticRegression,
                      RandomForestClassifier,
                      LinearSVC,
                      SGDClassifier]
        model_names = ["LogReg", "RF Clas.", "LinearSVC", "SGD Clas."]
        
    if not vectorizer_cls or not model_names:
        vectorizer_cls = [TfidfVectorizer, CountVectorizer]
        vectorizer_names = ["TfidfVec", "CntVec"]
       
    vectorizer_names = iter(vectorizer_names)
    for vectorizer in vectorizer_cls:
        vector_name = next(vectorizer_names)
        model_names = iter(model_names)
        model_score = list()
        for model in models_cls:
            pipe = build_pipe(vectorizer, model, stopwords=stopwords,
                              ngram_range=ngram_range, min_df=min_df)
            score = cross_val_score(pipe, X_train, y_train, scoring='accuracy', cv=cv)
        
            mean.append(np.mean(score))
            model_score.append(score)
            worked_models.append(next(model_names) + vector_name)
        scores.append(model_score)
    return worked_models, mean, scores
