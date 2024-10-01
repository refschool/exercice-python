#https://datacorner.fr/audio-recog/
import speech_recognition as sr
filename = "16-122828-0002.wav"
filename = "test.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data,language="fr-FR")
    print(text)