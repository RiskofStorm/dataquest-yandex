from dump_models import serialize_model
from flask import Flask, render_template, request
from sentiment_classifier import LoadedModel

app = Flask(__name__)


# Reviews with less than 100 words probably would count as negative, since model learned on heavy reviews
# You can see samples of reviews(text) in model_test.py


@app.route("/test")
def test():
    return "Wake up and smell the ashes"

# Actuall app
@app.route("/", methods=["POST", "GET"])
def main_page(text='', prediction_msg=''):
    if request.method == "POST":
        text = request.form['text']
        print(text)
        prediction_msg = loadedModel.process(text)
        print(prediction_msg)
    return render_template("result.html", text=text, prediction_msg=prediction_msg)


if __name__ == "__main__":
    print("Checking serialized word_converter, model: ", end="")
    try:
        with open("./LogReg.pkl", "rb") as f:
            pass
        with open("./CountVect.pkl", "rb") as m:
            pass
        print("FOUND")
    except FileNotFoundError:
        print("NOT FOUND")
        print("Process data, train word_converter, model: ", end="")
        serialize_model()
        print("DONE -- RESTART main.py !!")
        raise SystemExit

    print("Loading word_converter, model: ", end="")
    loadedModel = LoadedModel()
    print("LOADED")
    print(" ")
    print(" ")
    app.debug = False
    app.run()

