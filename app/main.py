from flask import Flask, request, jsonify
import preprocess.app.preprocessing as prep

app= Flask(__name__)


@app.route('/')
def index():
  return "<h1>Fatih Legend 4</h1>"

@app.route('/preprocess-one-sentence',methods=['POST'])
def preprocess_one_sentence():
    req_data = request.get_json()
    text = req_data['text']
    preprocessed_text = prep.preprocess(text)
    return jsonify({
        "text": preprocessed_text
    })