import os
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from . import SpeakerFeatureExtractor

source = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/development_set"
modelpath = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/speaker_models"
voice_samples = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/voice_samples"
audio_path = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/temp_audio.wav"

# Load the Models
model_files = [os.path.join(modelpath, fname) for fname in
             os.listdir(modelpath) if fname.endswith('.gmm')]

models = [cPickle.load(open(fname, 'rb')) for fname in model_files]
speakers = [fname.split("\\")[-1].split(".gmm")[0] for fname
            in model_files]

current_speaker_system_label = 0
recognized_speakers = []


def speaker_change_detector():
    global current_speaker_system_label, recognized_speakers

    sr, audio = read(audio_path)
    vector = SpeakerFeatureExtractor.extract_features(audio, sr)

    log_likelihood = np.zeros(len(models))

    for i in range(len(models)):
        model = models[i]  # checking with each model one by one
        scores = np.array(model.score(vector))
        log_likelihood[i] = scores.sum()

    winner = np.argmax(log_likelihood)
    print(current_speaker_system_label)
    score = log_likelihood + 100
    return winner, score


def speaker_change_detector_from_post_data(data):
    return 0, 0

