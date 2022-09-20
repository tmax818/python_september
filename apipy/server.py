import re
from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)

@app.route("/<item>")
def index(item):
    data = requests.get(f"https://rickandmortyapi.com/api/{item}")
    pprint(data.json())
    return render_template('index.html', data = data.json())

if __name__ == "__main__":
    app.run(debug=True)