import google.generativeai as genai
import openai
from Services.ListenAndSpeak import Speak
from Services.api_key import api_key
genai.configure(api_key = api_key1)

def AI(query):
    try:
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 512,
        }

        model = genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config)
        
        convo = model.start_chat()
        convo.send_message(query)
        resp = (convo.last.text).replace('*', ' ')
        Speak(resp)
    except:
        chatStr = ""
        openai.api_key = apikey2
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


