from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# TODO add all supported types
ALLOWED_EXTENSIONS = {'wav'}


def is_valid_extension(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# TODO ensure I am using the correct error codes
@app.route("/genre", methods=["POST"])
@cross_origin()
def detect_genre():
    if "file" not in request.files:
        return "No file provided", 500

    file = request.files["file"]
    filename = secure_filename(file.filename)

    if filename == '' or not file:
        return "No file provided", 500

    if not is_valid_extension(filename):
        return "Invalid file extension", 500

    return "hello"


"""
TODO Routes:
- genres
- lyricgen
"""

if __name__ == "__main__":
    app.run(debug=True)
