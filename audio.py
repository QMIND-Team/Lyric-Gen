import librosa
import matplotlib.pyplot as plt
import librosa.display
from pandas import DataFrame

def extract_info(audio_fname):
    x , sr = librosa.load(audio_fname,sr=44100)
    seconds = len(x)/sr

    # zero_crossings is a bool array
    zero_crossings = sum(librosa.zero_crossings(x,pad=False))
    zero_crossing_rate = zero_crossings / seconds

    return (audio_fname,zero_crossing_rate)


audio_paths = ['sound.wav']
data = list(map(extract_info,audio_paths))
df = DataFrame(data,columns=('Filename','ZeroCrossingRate'))
print(df)
