import pyaudio
from deepspeech import Model
import scipy.io.wavfile as wav
import wave
import deepspeech as ds
import glob

# The global variables required for the configuration of Speech Transcription
WAVE_OUTPUT_FILENAME = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/temp_audio.wav"
testAudio = "8455-210777-0068.wav"
DIR_NAME = "C:/Users/HARI/PycharmProjects/HaSaSystem/Main/Main/Resources/deepspeech-0.6.1-models"
N_FEATURES = 25
N_CONTEXT = 9
BEAM_WIDTH = 500
LM_ALPHA = 0.75
LM_BETA = 1.85
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5


def resolve_models(dirName):
    pb = glob.glob(dirName + "/*.pb")[0]
    print("Found Model: %s" % pb)

    lm = glob.glob(dirName + "/lm.binary")[0]
    trie = glob.glob(dirName + "/trie")[0]
    print("Found Language Model: %s" % lm)
    print("Found Trie: %s" % trie)

    return pb, lm, trie


args = resolve_models(DIR_NAME)
ds = Model(args[0], BEAM_WIDTH)
ds.enableDecoderWithLM(args[1], args[2], LM_ALPHA, LM_BETA)


def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording................")

    frames = [stream.read(CHUNK) for i in range(0, int(RATE / CHUNK * RECORD_SECONDS))]

    print("Inferring................")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def predict_from_input(data):
    # fs, audio = wav.read(WAVE_OUTPUT_FILENAME)
    # return ds.stt(audio)
    print("Inferring from the input from post.......")


def predict():
    record_audio()
    fs, audio = wav.read(WAVE_OUTPUT_FILENAME)
    return ds.stt(audio)
