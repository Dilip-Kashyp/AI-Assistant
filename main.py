import datetime
import openai
import requests
import speech_recognition as mic
import win32com.client
import webbrowser
import pywhatkit
from api_key import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr = ""


def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query}\n AI Assistant:"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatStr += f"{response['choices'][0]['text']}\n"
    print(chatStr)
    speaker.Speak(response["choices"][0]["text"])

    return response["choices"][0]["text"]


def listening():
    print("Listening.......")
    reco = mic.Recognizer()
    with (mic.Microphone() as source):
        audio = reco.listen(source)
        try:
            print("Recognizing......")
            query = reco.recognize_google(audio, language='eng-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return 'An exception occurred: %s', e


if __name__ == '__main__':
    speaker.Speak("Hiiii, i am AI Assistant, How Can i help you sirr..")
    while True:
        query = listening()
        if f"Sorry".lower() in query:
            listening()

        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                 ["wikipedia", "https://www.wikipedia.com"], ["facebook", "https://www.facebook.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir.....")
                webbrowser.open(site[1])
                speaker.Speak("Anything else sirr....")
        if "play" in query.lower():
            song = query.replace('play', ' ')
            speaker.Speak("Playing" + song)
            pywhatkit.playonyt(song)
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speaker.Speak(f"sirr the time is {time}")
        elif "send a whatsapp" in query.lower():
            speaker.Speak("Who to send the message to? sirr..")
            receiver = listening()
            speaker.Speak("What is the message, sirr..")
            message = listening()
            pywhatkit.sendwhatmsg_instantly("+918950369581", f"{message}")
        elif "news" in query.lower():
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=69976b6b305f4a8f9c7fc83b76de3c3f"
            news = requests.get(url).json()
            articles = news['articles']
            news_articles = []
            for article in articles:
                news_articles.append(article['title'])
            for i in range(5):
                speaker.Speak(news_articles[i])
                print(i+1, news_articles[i])
        elif "thank you".lower() in query.lower():
            speaker.Speak("Most welcome sir.....")
            exit()
        else:
            chat(query)
