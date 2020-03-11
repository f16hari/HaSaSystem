from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('InferFromAudioInput', views.InferFromAudioInput, name='InferFromAudioInput'),
    path('InferAudioFromServer', views.InferAudioFromServer, name='InferAudioFromServer')
]

