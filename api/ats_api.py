from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
import logging
import json

# -----------------------------
# App Setup
# -----------------------------
app = Flask(__name__)
CORS(app)

# -----------------------------
# Folders
# -----------------------------
UPLOAD_FOLDER = "uploads"
LOG_FOLDER = "logs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "ats.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Upload API
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    filename = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    logging.info(f"Uploaded file: {filename}")

    return jsonify({
        "message": "Resume uploaded",
        "file": filename
    })


# -----------------------------
# Parse API
# -----------------------------
@app.route("/parse", methods=["POST"])
def parse_resume():

    data = request.json

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    file = data.get("file")

    if not file:
        return jsonify({"error": "file required"}), 400

    logging.info(f"Parsed file: {file}")

    return jsonify({
        "status": "parsed",
        "file": file
    })


# -----------------------------
# Score API
# -----------------------------
@app.route("/score", methods=["POST"])
def score_candidate():

    data = request.json or {}

    role = data.get("role", "data analyst")

    score = 0.78

    return jsonify({
        "role": role,
        "ats_score": score
    })


# -----------------------------
# Shortlist API
# -----------------------------

@app.route("/shortlist", methods=["GET"])
def shortlist():

    ranked_file = "data/ranked_candidates/ranked.json"

    if not os.path.exists(ranked_file):
        return jsonify({"error": "ranked file not found"}), 404

    with open(ranked_file, "r") as f:
        ranked = json.load(f)

    shortlisted = [
        r for r in ranked
        if r.get("status") == "SHORTLISTED"
    ]

    return jsonify({
        "shortlisted_candidates": shortlisted
    })

# -----------------------------
# Async Job Status
# -----------------------------
jobs = {}

@app.route("/job/<job_id>", methods=["GET"])
def job_status(job_id):

    status = jobs.get(job_id, "processing")

    return jsonify({
        "job_id": job_id,
        "status": status
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "ATS API Running",
        "endpoints": [
            "/upload",
            "/parse",
            "/score",
            "/shortlist",
            "/job/<id>"
        ]
    })
# -----------------------------
# Error Handler
# -----------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "endpoint not found"}), 404


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    print("Starting ATS API...")
    print("Server running at: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)