from flask import Flask, request, jsonify
import json
import app.preprocessing as prep

app= Flask(__name__)


@app.route('/')
def index():
  return "<h1>Fatih Legend 4</h1>"

@app.route('/preprocess-one-sentence',methods=['POST'])
def preprocess_one_sentence():
    req_data = request.get_json()
    siswa = req_data['siswa']
    dosen = req_data['dosen']
    preprocessed_text_siswa = prep.preprocess(siswa)
    preprocessed_text_dosen = prep.preprocess(dosen)
    return jsonify({
        "siswa": preprocessed_text_siswa,
        "dosen": '؛'.join(preprocessed_text_dosen)
    })

@app.route('/preprocess-all',methods=['POST'])
def preprocess_all():
  req_data = request.get_json()
  preprocessed = []
  for answer in req_data:
    name = answer['name']
    answers = answer['answers']
    preprocessed_answers = prep.preprocess_all(answers)
    preprocessed.append({
      'name' : name,
      'answers': preprocessed_answers
    })
  return json.dumps(preprocessed, ensure_ascii=False)

