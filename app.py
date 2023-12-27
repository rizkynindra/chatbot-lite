import mimetypes
import os.path

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from chat import get_response
import nltk

nltk.download('punkt')


scriptPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptPath)
template_folder = os.path.join(os.getcwd(),'templates')
static_folder = os.path.join(os.getcwd(),'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
CORS(app)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path, mimetype='text/css')

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)