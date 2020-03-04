import speech_recognition as sr

def return_voice():
    print('running')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except:
            return -1
