from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls),
    path('speech-recognition/', include('speech_recognition.urls')),
]
