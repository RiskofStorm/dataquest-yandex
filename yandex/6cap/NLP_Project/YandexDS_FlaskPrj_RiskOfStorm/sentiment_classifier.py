from sklearn.externals import joblib


class LoadedModel:
    def __init__(self):
        self.model = joblib.load("./LogReg.pkl")
        self.vectorizer = joblib.load("./CountVect.pkl")
        self._pred_result = {0: "negative", 1: "positive", -1: "prediction error"}

    @staticmethod
    def __proba_descript(prob):
        if prob <= .55:
            return "unlikely"
        elif prob >= .56:
            return "most likely"
        elif prob >= .95:
            return "certain"
        else:
            return "something went wrong"

    def __predict(self, text):
        try:
            text = self.vectorizer.transform([text])
            return self.model.predict(text)[0], self.model.predict_proba(text[0]).max()
        except:
            print("Error occurred")
            return -1, 1

    def process(self, text):
        result = self.__predict(text)
        return "Sentence sentiment - {0}, Probability: {1} - {2}%".format(self._pred_result[result[0]],
                                                                          self.__proba_descript(float(result[1])),
                                                                          str(round(result[1], 3)))
