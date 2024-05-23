import speech_recognition as sr
import pyaudio
from pycaw.pycaw import AudioUtilities
from volume_control import AudioController
import os
import sys

# prints a list of audio devices
def get_devices(p: pyaudio.PyAudio):
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
def desktop_input(p: pyaudio.PyAudio, txt_file: str):
    print("Now recording desktop audio...")
    CHUNK = 1024
    subtitles = open(txt_file, "a")
    stream = p.open(format= pyaudio.paInt16,
                    channels= 2,
                    rate= 44100,
                    input= True,
                    input_device_index= None,
                    frames_per_buffer = CHUNK,
                    )
    while True:
        try:
            eng_sub = stream.read(CHUNK)
            subtitles.write(eng_sub)
        except: 
            print("Error writing to file...")
    subtitles.close()
    stream.close()
    p.terminate()

def video_input():
    pass

# gets volume of audio stream
def volume_check():
    pass

# translates audio to english
def translate(input):
    pass
    
if __name__ == "__main__":
    p = pyaudio.PyAudio()
    #get_devices(p)
    desktop_input(p, "E:\Projects-Python\Audio-Adjustment-App\subtitles.txt")