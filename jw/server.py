from flask import Flask, jsonify, render_template
from data import fours, fives
from random import choice

picks = [fours, fives]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', thing = choice(choice(picks)))

if __name__ == "__main__":
    app.run(debug=True)