from flask import Flask, request, jsonify, send_from_directory
import os
from utils.mcaddon_utils import handle_upload
from utils.bds_sync import sync_packs
from utils.world_utils import list_worlds

app = Flask(__name__, static_folder='frontend')

# Serve static files (HTML, CSS, JS)
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        result = handle_upload(file)
        return jsonify(result)
    return "No file uploaded", 400

@app.route('/sync', methods=['POST'])
def sync():
    result = sync_packs()
    return jsonify(result)

@app.route('/worlds', methods=['GET'])
def worlds():
    return jsonify(list_worlds())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
