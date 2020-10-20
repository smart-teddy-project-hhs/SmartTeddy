from django.urls import path

from . import views

app_name = 'speech_recognition'
urlpatterns = [
    path('sentence', views.sentence, name='sentence'),
]
