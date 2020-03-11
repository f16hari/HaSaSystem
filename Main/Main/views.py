from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def Home(request):
    return  HttpResponse("Hello World ")

@csrf_exempt
def InferFromAudioInput(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        print(json.loads(data))
        return HttpResponse("Infering from input.......")

@csrf_exempt
def InferAudioFromServer(request):
    return HttpResponse("Infering from the audio input from server........")