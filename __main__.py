import speech_recognition as sr
from googletrans import Translator
import pyaudio
import os
import sys

# prints a list of audio devices
def get_devices(p):
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

# opens desktop audio stream
def desktop_input(p):
    subtitles = open("subtitles.txt", "a")
    stream = p.open(format= pyaudio.paInt16,
                    channels= 2,
                    rate= 44100,
                    input= True,
                    #input_device_index= None,
                    frames_per_buffer = 1024,
                    )
    subtitles.close()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    translator = Translator()
    p = pyaudio.PyAudio()
    get_devices(p)
    desktop_input(p)
