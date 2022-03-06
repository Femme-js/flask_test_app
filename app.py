from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, world!'



if __name__ == "__main__":
    app.run(debug=True)