from flask import Flask

app = Flask(__name__)

@app.route("/genre")
def detect_genre():
    return {"result": 0}

"""
TODO Routes:
- genres
- lyricgen
"""

if __name__ == "__main__":
    app.run(debug=True)