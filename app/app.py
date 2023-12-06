from flask import Flask, render_template,request
from model import predict_player1, predict_player2

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
        result1 = predict_player1(text)
        result2 = predict_player2(text)
        return render_template('predict.html',result1 = result1, result2 = result2)

if __name__ == "__main__":
    app.run(debug = True)
