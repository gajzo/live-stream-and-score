#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Live Cricket Score App - Enhanced Version Running!"

@app.route('/api/status')
def status():
    return jsonify({
        "status": "running",
        "version": "enhanced",
        "features": [
            "auto-refresh",
            "batsman-details", 
            "bowler-stats",
            "team-highlighting",
            "balls-remaining"
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)