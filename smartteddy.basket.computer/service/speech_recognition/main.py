#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os

voicemodel = "medium_model_nl"

if not os.path.exists(voicemodel):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio
import requests
import json

model = Model(voicemodel)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        request_header = {'Content-Type': 'application/json'}
        r = requests.post(
            'http://localhost:8000/speech-recognition/sentence',
            data=rec.Result(),
            headers=request_header
        )
        print('requests status code: {0}'.format(r.status_code))
        # TODO get result when involving special characters
        print("begin result")
        print(rec.Result())
        print("end result")
    else:
        print(rec.PartialResult())

print(rec.FinalResult())





