import datetime
from openai import OpenAI
import requests
from secret import api_key, my_bot_id, local_masjids, halal_options

API_KEY = api_key
client = OpenAI(api_key=API_KEY)

def say_something():

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": "make a random announcement"}],
        max_tokens=150,
        n=1
    )
    bot_response = response.choices[0].message.content.strip("\n").strip()

    url = "https://api.groupme.com/v3/bots/post"
    bot_response = bot_response
    data = {
        "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
        "text": bot_response
    }
    response = requests.post(url, json=data)

if datetime.datetime.today().weekday() == 2:
    say_something()