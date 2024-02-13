import requests
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import os

CHAT_GPT_API = os.getenv('CHAT_GPT_API')

def get_random_duck():
    endpoint = "https://random-d.uk/api/random"
    response = requests.get(endpoint)
    data = response.json()
    return data['url']

def get_random_cat():
    endpoint1 = "https://api.thecatapi.com/v1/images/search"
    response1 = requests.get(endpoint1)
    data1 = response1.json()
    return data1[0]['url']

def get_random_dog():
    endpoint2 = "https://dog.ceo/api/breeds/image/random"
    response2 = requests.get(endpoint2)
    data2 = response2.json()
    return data2["message"]

def get_random_clearbit():
    endpoint3 = "https://logo.clearbit.com/segment.com"
    return endpoint3

def get_random_photo():
    endpoint4 = "https://source.unsplash.com/random"
    return endpoint4

    
def get_chatGPT_response(question):
    url = "https://api.openai.com/v1/chat/completions"
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {CHAT_GPT_API}"}
    data = {"model": "gpt-3.5-turbo","messages": [{"role": "user","content": question}]}
    response = requests.post(url, headers=header, json=data)
    print(response.status_code)
    print(response.json())
    # return data['choices'][0]['message']['content']
