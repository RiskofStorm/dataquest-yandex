
def process_data(data, func):
    pr_data = data.copy()
    index = data.shape[0]
    for i in range(index):
        pr_data[i] = " ".join([func(w) for w in data[i].split()])
    return pr_data


def build_pipe(vect, model, stopwords=None, ngram_range=(1,1), analyzer='word'):
    return Pipeline([("count", vect(stop_words=stopwords, ngram_range=ngram_range, analyzer=analyzer)),
                     ("model", model())])


def train_test_models(X_train, y_train, models_cls=None, vectorizer_cls=None, 
                      random_state=None, min_df=None,stopwords=None,
                      ngram_range=(1,1), analyzer='word',
                      vectorizer_names=None, models_names=None):
    results = list()
    mean = list()
    if not models_cls or not vectorizer_names:
        models_cls = [LogisticRegression,
                      RandomForestClassifier,
                      LinearSVC,
                      SGDClassifier]
        models_names = ["LogReg", "RF Clas.", "LinearSVC", "SGD Clas."]
    if not vectorizer_cls or not model_names:
        vectorizer_cls = [TfidfVectorizer, CountVectorizer]
        vectorizer_names = ["TfidfVec", "CntVec"]
       
    _vectorizer_names = iter(vectorizer_names)
    for vectorizer in vectorizer_cls:
        vector_name = _vectorizer_names.__next__()
        _model_names = iter(models_names)
        for model in models_cls:
            pipe = build_pipe(vectorizer, model, stopwords=stopwords,
                              ngram_range=ngram_range, analyzer=analyzer)
            score = cross_val_score(pipe, X_train, y_train, scoring='accuracy')
            mean.append(np.mean(score))
            results.append("model: {}, vectorizer: {}  scores: {}, mean: {}".format(_model_names.__next__(),
                                                                                       vector_name, score,
                                                                                       round(np.mean(score),4)))
            
    return results, mean
