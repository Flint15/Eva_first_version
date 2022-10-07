import vosk
import sys
import queue
import json
import sounddevice as sd
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

model = vosk.Model("model")
samplerate = 16000
device = 1

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(voice):
    try:
        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype="int16",
                               channels=1, callback=callback):
            
            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    query = json.loads(rec.Result())["text"]
                    return query
    except:
        return None

def record_volume():    
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        print(query)
        return query

