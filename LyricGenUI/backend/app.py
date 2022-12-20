from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import soundfile
import librosa
import numpy as np
import keras
from keras import Sequential

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# TODO add all supported types
ALLOWED_EXTENSIONS = {'wav'}
GENRE_MODEL: Sequential = keras.models.load_model("./models/genre")


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

    # Process file
    sfo = soundfile.SoundFile(file)
    y, sr = librosa.load(sfo, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    raw = np.array([np.mean(chroma_stft), np.mean(rms), np.mean(spec_cent), np.mean(
        spec_bw), np.mean(rolloff), np.mean(zcr), *[np.mean(i) for i in mfcc]])
    data = raw.reshape(1, -1)[0:1, :]

    res = GENRE_MODEL.predict(data)
    return {"result": int(np.argmax(res[0]))}


"""
TODO Routes:
- genres
- lyricgen
"""

if __name__ == "__main__":
    app.run(debug=True)
