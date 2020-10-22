from django.urls import path

from . import views

app_name = 'speechrecognition'
urlpatterns = [
    path('sentence', views.sentence, name='sentence'),
]
