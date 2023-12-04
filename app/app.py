from flask import Flask, render_template,request
from model import predict_player

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/show', methods=["GET", "POST"])
def show():
    return render_template('show.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        text = request.form["text"]
        print(text)
        result = predict_player(text)
        return render_template('predict.html',result = result)

if __name__ == "__main__":
    app.run(debug = True)
