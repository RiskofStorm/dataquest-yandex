
def build_pipe(vect, model, stopwords=None, ngram_range=(1,1), min_df=3):
    return Pipeline([("count", vect(stop_words=stopwords, ngram_range=ngram_range, 
                                    min_df=min_df)),
                     ("model", model())])

def text_cleaning(series):
    # This func clears text from symbols. 
    # Returns Series -> Series[row] = list of words:str
    for i in range(series.shape[0]):
        text = series.iloc[i]
        pattern = re.compile(r"(?u)\w+")
        series.iloc[i] = re.findall(pattern, text.lower())
    return series

def apply_to_str(data, func):
    # This func applies given func to every word
    # Returns Series -> Series[row] = text:str
    series = data.copy()
    for i in range(data.shape[0]):
        series.iloc[i] = " ".join([func(w) for w in data.iloc[i]])
    return series

def handle_rawdata(X_train, X_test, X_full=None, func=None):
    # Appiles apply_to_str, text_cleaning functions to given Series
    if not X_full:
        X_full = X_train.append(X_test)
    if not func:
        raise AssertionError("No function given!")
        
    pr_data = list()
    for data in [X_train, X_test, X_full]:
        pr_data.append(apply_to_str(text_cleaning(data), func))
    return pr_data

def train_test_models(X_train, y_train, cv=3, models_cls=None, vectorizer_cls=None, 
                      random_state=None, min_df=None,stopwords=None, 
                      ngram_range=(1,1), model_names=None, vectorizer_names=None):
    results = list()
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
       
    _vectorizer_names = iter(vectorizer_names)
    for vectorizer in vectorizer_cls:
        vector_name = _vectorizer_names.__next__()
        _model_names = iter(model_names)
        model_score = list()
        for model in models_cls:
            pipe = build_pipe(vectorizer, model, stopwords=stopwords,
                              ngram_range=ngram_range, min_df=min_df)
            score = cross_val_score(pipe, X_train, y_train, scoring='accuracy',cv=cv)
            
            mean.append(np.mean(score))
            model_score.append(score)
            results.append("model: {}, vectorizer: {}, scores: {}, mean: {}".format(
                                                            _model_names.__next__(),
                                                             vector_name, score,
                                                             round(np.mean(score),4)))
        scores.append(model_score)
    return results, mean, scores
