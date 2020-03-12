from . import SpeechTranscription
from . import LabelExtractor


def infer_from_post_input(data):
    text = SpeechTranscription.predict_from_input(data)
    names = LabelExtractor.get_human_names(text.title())
    if len(names) != 0:
        label = names[0]
    else:
        label = ""

def infer_from_server_audio():
    text = SpeechTranscription.predict()
    names = LabelExtractor.get_human_names(text.title())
    if len(names) != 0:
        label = names[0]
    else:
        label = ""
    print("Label : {0} Text : {1}".format(label, text))
