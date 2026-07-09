from flask import Flask, send_from_directory, jsonify, request
import os

# Root directory එක - index.html එක තියෙන්නේ api folder එකෙන් එලියේ
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder=ROOT_DIR, static_url_path='')

@app.route('/')
def home():
    """
    Main page - index.html එක serve කරනවා
    """
    return send_from_directory(ROOT_DIR, 'index.html')

@app.route('/api/popular')
def get_popular():
    """
    Popular movies return කරන fake API එකක්
    Frontend එකෙන් /api/popular call කරාම මේ data ටික යනවා
    """
    movies = [
        {
            "id": 1,
            "title": "Inception",
            "year": 2010,
            "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg",
            "rating": 8.8,
            "subtitle": "Sinhala"
        },
        {
            "id": 2,
            "title": "Avatar",
            "year": 2009,
            "poster": "https://m.media-amazon.com/images/M/MV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg",
            "rating": 7.9,
            "subtitle": "Sinhala"
        },
        {
            "id": 3,
            "title": "The Dark Knight",
            "year": 2008,
            "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
            "rating": 9.0,
            "subtitle": "Sinhala"
        },
        {
            "id": 4,
            "title": "Interstellar",
            "year": 2014,
            "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
            "rating": 8.6,
            "subtitle": "Sinhala"
        }
    ]
    return jsonify(movies)

@app.route('/api/search')
def search_movies():
    """
    Search API එක - දැන් Inception, Avatar type කරලා search කරොත් result එනවා
    """
    query = request.args.get('q', '').lower()
    
    all_movies = [
        {
            "id": 1,
            "title": "Inception",
            "year": 2010,
            "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg",
            "rating": 8.8,
            "subtitle": "Sinhala"
        },
        {
            "id": 2,
            "title": "Avatar",
            "year": 2009,
            "poster": "https://m.media-amazon.com/images/M/MV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg",
            "rating": 7.9,
            "subtitle": "Sinhala"
        }
    ]
    
    # Search query එකට match වෙන movies filter කරනවා
    if query:
        results = [m for m in all_movies if query in m['title'].lower()]
        return jsonify(results)
    else:
        return jsonify([])

@app.route('/<path:path>')
def serve_static(path):
    """
    CSS, JS, Images වගේ static files serve කරනවා
    උදා: /style.css, /script.js, /images/logo.png
    """
    if os.path.exists(os.path.join(ROOT_DIR, path)):
        return send_from_directory(ROOT_DIR, path)
    else:
        return "404 - File Not Found", 404

# Replit එකටයි local test වලටයි
if __name__ == '__main__':
    # Replit එකට port 5000 ඕන
    app.run(host='0.0.0.0', port=5000, debug=False)
