from flask import Flask, request
import prep

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Fatih Legend 4</h1>"

@app.route('/preprocess-one-sentence',methods=['POST'])
def preprocess_one_sentence():
    req_data = request.get_json()
    text = req_data['text']
    preprocessed_text = prep.preprocess(text)
    return {
        "text": preprocessed_text
    }