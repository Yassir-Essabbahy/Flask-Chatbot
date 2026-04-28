from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import uuid
import requests
import logging

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyDYk0ZervoN1ztSx66CQD0X9jqmq9kJhrQ"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

conversations = {}
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["GET"])
def start_conversation():
    thread_id = str(uuid.uuid4())
    conversations[thread_id] = []
    return jsonify({"thread_id": thread_id})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        thread_id = data.get("thread_id")
        message = data.get("message")

        if not thread_id or not message:
            return jsonify({"error": "Missing data"}), 400

        if thread_id not in conversations:
            conversations[thread_id] = []

        payload = {
            "contents": [{"parts": [{"text": message}]}]
        }

        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": API_KEY
        }

        response = requests.post(ENDPOINT, headers=headers, json=payload)
        result = response.json()
        reply = result['candidates'][0]['content']['parts'][0]['text']

        conversations[thread_id].append({"role": "user", "message": message})
        conversations[thread_id].append({"role": "bot", "message": reply})

        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
