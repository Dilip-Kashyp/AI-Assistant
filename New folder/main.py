import datetime
import speech_recognition as mic
import pyttsx3
import openai
from api_key import  api_key2


def AI(query):
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
    presence_penalty=0)
    chatStr += f"{response['choices'][0]['text']}\n"
    chatStr = ""
    Speak(response["choices"][0]["text"])
        

def Speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.setProperty('rate',130)
    volume = engine.getProperty('volume', volume)
    engine.say(audio)
    print(audio)
    engine.runAndWait() 


def listening():
    status = "Wait, Starting Mic..."
    print(f"{status}")
    reco = mic.Recognizer()
    with mic.Microphone() as source:
        reco.adjust_for_ambient_noise(source)
        reco.pause_threshold = 1
        reco.energy_threshold = 300
        status = "Speak now Listening......."
        print(f"{status}")
        audio = reco.listen(source)
    try:
        print("Recognizing......")
        query = reco.recognize_google(audio, language='eng-in')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        return 'sorry, try again, speak clearly'


if __name__ == '__main__':
    Speak("Hiii, I am an AI Assistant. How can i help you")
    while True:
        query = listening()
        if "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            Speak(f"The time is {time}")    
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
            exit()
        else:
            AI(query)
