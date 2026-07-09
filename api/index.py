from flask import Flask, send_from_directory, jsonify
import os

# Root directory එක හොයාගන්නවා - index.html එක තියෙන්නේ api folder එකෙන් එලියේ
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder=ROOT_DIR, static_url_path='')

@app.route('/')
def home():
    """
    Main page - index.html එක serve කරනවා
    """
    return send_from_directory(ROOT_DIR, 'index.html')

@app.route('/api/hello')
def hello():
    """
    Test API endpoint එකක්
    Browser එකේ /api/hello ගහලා බලපන් {"message": "Hello"} එනවද කියලා
    """
    return jsonify({"message": "Hello from Flask!", "status": "success"})

@app.route('/<path:path>')
def serve_static(path):
    """
    CSS, JS, Images වගේ static files serve කරනවා
    උදා: /style.css, /script.js, /images/logo.png
    """
    # File එක root එකේ තියනවද බලනවා
    if os.path.exists(os.path.join(ROOT_DIR, path)):
        return send_from_directory(ROOT_DIR, path)
    else:
        return "404 - File Not Found", 404

# Replit එකටයි local test වලටයි
if __name__ == '__main__':
    # 0.0.0.0 දාන්නේ Replit එකට public access දෙන්න
    # Port 8080 Replit එකේ default
    app.run(host='0.0.0.0', port=8080, debug=True)
