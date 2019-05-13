from dump_models import serialize_model
from sentiment_classifier import LoadedModel
from flask import render_template, request
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"]
app_dash = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                     url_base_pathname='/plot/')
app = app_dash.server


@app.route("/test")
def test():
    return "Wake up and smell the ashes"


@app.route("/", methods=["POST", "GET"])
def main_page(text='', prediction_msg=''):
    if request.method == "POST":
        text = request.form['text']
        print(text)
        prediction_msg = loadedModel.process(text)
        print(prediction_msg)
    return render_template("result.html", text=text, prediction_msg=prediction_msg)


@app.route("/plot/")
def model_stats():
    return app_dash.index()


@app.route("/words/")
def model_words():
    mvw = loadedModel.get_stats()[1]
    mvw = "\n".join(["{} : {}".format(i[0], i[1]) for i in mvw[::-1]])
    return render_template("words.html", words="WORD : FREQUENCY \n \n" + mvw)


@app.route("/model/")
def model():
    return render_template("model.html", model=loadedModel.model)


if __name__ == "__main__":
    print("Checking serialized word_converter, model, stats: ")
    try:
        with open("./model.pkl", "rb") as r:
            print('FOUND MODEL')
        with open("./vectorizer.pkl", "rb") as f:
            print("FOUND VECTORIZER")
        with open('./model_stats.pkl', 'rb') as m:
            print("FOUND MODEL STATS")

    except FileNotFoundError:
        print("SOMETHING IS MISSING")
        print("Process data, train vectorizer and model, gathering stats: ")
        serialize_model()
        print("DONE >>>> RESTART main.py ")
        raise SystemExit

    print("LOADING: vectorizer, model, stats")
    loadedModel = LoadedModel()

    most_valuable_features, most_valuable_words = loadedModel.get_stats()
    _x, _y = zip(*most_valuable_words)
    max_words = 50
    app_dash.layout = html.Div(children=[dcc.Graph(id='a_graph',
                                                   figure={
                                                       'data': [go.Bar(name="Words Frequency",
                                                                       y=_x[:max_words],
                                                                       x=_y[:max_words],
                                                                       orientation='h',
                                                                       )
                                                                ],
                                                       'layout': go.Layout(
                                                           title='Most valuable words in model',
                                                           xaxis={"automargin": True},
                                                           yaxis={"automargin": True},
                                                           height=2100,
                                                           font=dict(family='Courier New, monospace', size=14,
                                                                     color='#000000')
                                                       )

                                                   })],
                               style={"margin": 50})

    print("LOADED")
    print("\n\n")
    app.debug = False
    app.run()
