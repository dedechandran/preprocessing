from flask import Flask, request, jsonify
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