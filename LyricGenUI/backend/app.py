from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/genre", methods=["POST"])
@cross_origin()
def detect_genre():
    print("Received request, responding...")
    return {"result": 0}


"""
TODO Routes:
- genres
- lyricgen
"""

if __name__ == "__main__":
    app.run(debug=True)
