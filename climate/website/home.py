#http://127.0.0.1:5000/ Home.html

import flask
from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

