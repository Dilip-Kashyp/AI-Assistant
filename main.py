import datetime
import openai
import requests
import speech_recognition as mic
import pyttsx3
import webbrowser
import pywhatkit
from bs4 import BeautifulSoup

from api_key import apikey



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.setProperty('rate',150)

    # for voice in voices:
    #    print(voice.id)
    #    engine.setProperty('voice', voices)
    #    engine.say("hello i am dilip")
    #    engine.runAndWait() 



def Speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait() 
    

def chat(query):
    chatStr = ""
    openai.api_key = apikey
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

    return response["choices"][0]["text"]


def listening():
    status = "wait, starting Mic..."
    print(f"{status}")
    reco = mic.Recognizer()
    with mic.Microphone() as source:
        reco.adjust_for_ambient_noise(source)
        reco.pause_threshold = 1
        reco.energy_threshold = 300
        status = "Speak now"
        print(f"{status}")
        print("Listening.......")
        audio = reco.listen(source)
    try:
        print("Recognizing......")
        query = reco.recognize_google(audio, language='eng-in')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        return 'sorry, try again, speak clearly'


if __name__ == '__main__':
    Speak("Hello, i am Intelligent Assistant. How can i help you")
    while True:
        query = listening()
        if f"open" in query:
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
            ["wikipedia", "https://www.wikipedia.com"], ["facebook", "https://www.facebook.com"]]
            for site in sites:
                if f"open {site[0]}" in query:
                    Speak(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                    Speak("Anything else")
        elif "play" in query:
            song = query.replace('play', ' ')
            Speak("Playing" + song)
            pywhatkit.playonyt(song)
            Speak("Enjoy Song..")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            Speak(f"The time is {time}")
        elif "send a whatsapp" in query:
            Speak("Who to send the message to? ")
            receiver = listening()
            Speak("What is the message")
            message = listening()
            pywhatkit.sendwhatmsg_instantly("+919896351799", f"{message}")
            Speak("Message seading...")
        elif "news" in query:
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=69976b6b305f4a8f9c7fc83b76de3c3f"
            news = requests.get(url).json()
            articles = news['articles']
            news_articles = []
            for article in articles:
                news_articles.append(article['title'])
            for i in range(5):
                print(f"{i+1} {news_articles[i]}")
                engine.say(news_articles[i])
                engine.runAndWait() 
        elif "thank you" in query:
            Speak("Most welcome")
            exit()
        else:
            chat(query)





