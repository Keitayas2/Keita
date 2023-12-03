from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        text = request.form["text"]
        print(text)
        return render_template('predict.html')

@app.route('/show', methods=["GET", "POST"])
def show():
    if request.method == 'GET':
        return render_template('show.html')
    elif request.method == 'POST':
        text = request.form["input_text"]
        print(text)
        return render_template('show.html')

if __name__ == "__main__":
    app.run(debug = True)
