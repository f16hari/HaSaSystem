from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .bin import Main as system

def Home(request):
    return  HttpResponse("Hello World ")

@csrf_exempt
def InferFromAudioInput(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        system.infer_from_post_input(data)
        return HttpResponse("\nInference Complete.........................")

@csrf_exempt
def InferAudioFromServer(request):
    system.infer_from_server_audio()
    return HttpResponse("\nInference Complete.........................")
