#!/usr/bin/env python3

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os
import requests
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Mock enhanced data for demonstration
ENHANCED_MOCK_DATA = {
    "title": "AUS W vs IND W - 3rd Match Live",
    "update": "Live",
    "livescore": "AUS W 128-3 (25.4) vs IND W 225-9 (50.0)",
    "runrate": "CRR: 5.02 | RRR: 6.45",
    
    # Team information with highlighting
    "team1_name": "AUS W",
    "team1_score": "128",
    "team1_wickets": "3",
    "team1_overs": "25.4",
    "team1_is_batting": True,
    "team2_name": "IND W", 
    "team2_score": "225",
    "team2_wickets": "9",
    "team2_overs": "50.0",
    "team2_status": "225-9 (50.0 overs)",
    "team2_is_batting": False,
    
    # Enhanced batsman information
    "batterone": "Beth Mooney",
    "batsmanonerun": "45",
    "batsmanoneball": "(52)",
    "batsmanonesr": "86.54",
    "batsmanone_balls_faced": 52,
    "batsmanone_fours": 6,
    "batsmanone_sixes": 1,
    
    "battertwo": "Ellyse Perry",
    "batsmantworun": "28",
    "batsmantwoball": "(31)",
    "batsmantwosr": "90.32",
    "batsmantwo_balls_faced": 31,
    "batsmantwo_fours": 3,
    "batsmantwo_sixes": 0,
    
    # Enhanced bowler information
    "current_bowler": "Deepti Sharma",
    "bowler_name": "Deepti Sharma",
    "bowler_overs": "5.4",
    "bowler_runs": "28",
    "bowler_wickets": "1",
    "bowler_economy": "4.94",
    "bowler_maidens": "1",
    "bowler_dots": 18,
    
    # Over information
    "balls_remaining": 2,
    "current_over": "25.4",
    "balls_in_over": 4,
    "over_runs": 7,
    
    # Partnership information
    "partnership_runs": "73",
    "partnership_balls": 83,
    "partnership_rate": "5.27",
    
    # Match status
    "match_status": "Live",
    "target": 226,
    "runs_needed": 98,
    "balls_left_match": 146,
    "required_run_rate": "6.45",
    "overs_left": "24.2",
    
    # Additional info
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

@app.route('/')
def serve_index():
    """Serve the enhanced index.html"""
    return send_from_directory('.', 'index.html')

@app.route('/api/current-score')
def get_current_score():
    """Return enhanced mock cricket data"""
    # Try to get real data from the main backend first
    try:
        response = requests.get('http://localhost:5000/api/current-score', timeout=2)
        if response.status_code == 200:
            real_data = response.json()
            # Enhance real data with mock enhanced fields
            enhanced_data = {**ENHANCED_MOCK_DATA, **real_data}
            return jsonify(enhanced_data)
    except:
        pass
    
    # Return mock data with current timestamp
    ENHANCED_MOCK_DATA["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(ENHANCED_MOCK_DATA)

@app.route('/api/status')
def get_status():
    """API status endpoint"""
    return jsonify({
        "status": "running",
        "version": "enhanced_v2.0",
        "features": [
            "auto-refresh (15s)",
            "batsman-details",
            "bowler-stats", 
            "team-highlighting",
            "balls-remaining",
            "over-progress",
            "partnership-info",
            "enhanced-ui"
        ],
        "auto_refresh": True,
        "update_interval": 15
    })

@app.route('/live')
def serve_live():
    """Serve the enhanced live page"""
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"🏏 Enhanced Cricket Score App starting on port {port}")
    print(f"📊 Features: Auto-refresh, Enhanced UI, Player Stats, Team Highlighting")
    print(f"🔗 Access: http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)