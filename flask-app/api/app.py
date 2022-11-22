#main.py
from flask import Flask, jsonify, request
from db import get_songs

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
  app.run(debug=True)
