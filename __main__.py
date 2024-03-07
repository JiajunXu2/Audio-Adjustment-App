import speech_recognition as sr
from googletrans import Translator
import pyaudio
import os

translator = Translator()
p = pyaudio.PyAudio()

def get_devices():
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        print(str(i) + " : " + device_info["name"])

def mic_input():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now listening...")
        audio = r.listen(source)

    # recognize speech using Whisper
    try:
        print("Whisper captured the following audio:" + r.recognize_whisper(audio, language="english"))
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError:
        print("Could not request results from Whisper")

def desktop_input():
    stream = p.open()

if __name__ == "__main__":
    get_devices()
    # text is .txt file 