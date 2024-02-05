import speech_recognition as mic
import pyttsx3
import eel
import openai
from Services.api_key import api_key2

def Speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.setProperty('rate',130)
    engine.say(audio)
    print(audio)
    engine.runAndWait() 

@eel.expose
def textrepo(query):
    try:
        chatStr = ""
        openai.api_key = api_key2
        chatStr += f"Intelligent Assistant:"
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        chatStr += f"{response['choices'][0]['text']}\n"
        chatStr = ""
        Speak(response["choices"][0]["text"])
        
    except:
        print("try again")
