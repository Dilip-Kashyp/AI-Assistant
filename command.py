import datetime
from datetime import date
import requests
import webbrowser
import pywhatkit
import eel
from Services.ListenAndSpeak import Speak, listening
from Services.OpenAI import AI

@eel.expose
def Commands():
    Speak("Hiii, I am an AI Assistant. How can i help you")
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
            eel.ShowHood()
            exit()
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            Speak(f"The time is {time}")    
        elif "send a whatsapp" in query:
            Speak("Who to send the message to? ")
            receiver = listening()
            Speak("What is the message")
            message = listening()
            Speak("Message sending.....")
            pywhatkit.sendwhatmsg_instantly("+919896351799", f"{message}")
            Speak("Message sended")
            eel.ShowHood()
            exit()
        elif "news" in query:
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=69976b6b305f4a8f9c7fc83b76de3c3f"
            news = requests.get(url).json()
            articles = news['articles']
            news_articles = []
            for article in articles:
                news_articles.append(article['title'])
            for i in range(5):
                newss = f"{i+1} {news_articles[i]}"
                Speak(newss)
        elif "thank you" in query:
            Speak("Most welcome")
            eel.ShowHood()
            exit()
        else:
            AI(query)
