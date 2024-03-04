import speech_recognition as sr
from googletrans import Translator

def start():
    translator = Translator()
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now listening...")
        audio = r.listen(source)

    # recognize speech using ...
    try:
        pass
    except:
        pass

if __name__ == "__main__":
    start()