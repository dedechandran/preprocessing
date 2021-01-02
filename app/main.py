from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Fatih Legend 4</h1>"