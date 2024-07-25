import base64
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from worker import speech_to_text, text_to_speech, watsonx_process_message

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    # Add your logic here
    response = {"message": "Speech to text processing is not implemented yet"}
    return jsonify(response), 200

@app.route('/process-message', methods=['POST'])
def process_message_route():
    # Add your logic here
    response = {"message": "Message processing is not implemented yet"}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
