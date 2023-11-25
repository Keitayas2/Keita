from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/new', methods=["GET", "POST"])
def new():
    return render_template('new.html')

@app.route('/show', methods=["GET", "POST"])
def show():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug = True)
