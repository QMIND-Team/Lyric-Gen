import librosa
import matplotlib.pyplot as plt
import librosa.display
from pandas import DataFrame
import numpy as np

def extract_info(audio_fname):
    x,sr = librosa.load(audio_fname,sr=44100)

    chroma_stft = np.mean(librosa.feature.chroma_stft(x, sr=sr))
    spec_cent = np.mean(librosa.feature.spectral_centroid(x, sr=sr))
    spec_bw = np.mean(librosa.feature.spectral_bandwidth(x, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(x, sr=sr))
    zcr = np.mean(librosa.feature.zero_crossing_rate(x))
    mfcc = librosa.feature.mfcc(x, sr=sr)
    mfcc_avg = tuple(map(lambda x:np.mean(x),mfcc))

    return (audio_fname,chroma_stft,spec_cent,spec_bw,rolloff,zcr) + mfcc_avg


audio_paths = ['sound.wav']
data = list(map(extract_info,audio_paths))
cols = (
    'Filename',
    'ChromaFreqs',
    'SpectralCentroid','SpectralBandwidth','SpectralRolloff',
    'ZeroCrossingRate') + tuple(['mfcc'+str(i) for i in range(1,21)])
df = DataFrame(data,columns=cols)
print(df)
