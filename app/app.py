from flask import Flask, render_template,request
from model import predict_player1, predict_player2, get_player_name, get_player_image
import os

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
        text = request.form.getlist("text")
        positions = request.form.getlist("q1")
        print(text,positions)
        result1 = None  # デフォルトの値でresult1を初期化
        result2 = None  # デフォルトの値でresult2を初期化

        if not text or not text[0].strip():  # textが空または空白文字だけの場合
            msg = '検索テキストが入力されていません'
            return render_template('predict.html', msg=msg)

        if '野手' in positions:
            result1 = predict_player1(text[0])
            get_player_name(text[0])
        if '投手' in positions:
            result2 = predict_player2(text[0])
            get_player_name(text[0])
        if '野手' not in positions and '投手' not in positions:
            msg = 'ポジションが選択されていません'
            return render_template('predict.html',msg = msg)
        return render_template('predict.html',result1 = result1, result2 = result2)

if __name__ == "__main__":
    app.run(debug = True)
