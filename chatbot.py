import datetime
import requests
from flask import Flask, request
from openai import OpenAI
from secret import api_key, jummah_announcment, halal_options, local_masjids


API_KEY = api_key
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hello", 200


chat_log = [{"role": "system", "content": "Short witty responses: "}]

@app.route('/', methods=['POST'])
def webhook():
    global chat_log
    data = request.get_json()
    url = "https://api.groupme.com/v3/bots/post"

    if '.' in data['text'].lower()[0]:
        text = data['text'].lower()[1:]
        if len(chat_log) < 4:
            chat_log.append({"role": "user", "content": text})
        else:
            chat_log.pop(1)
            chat_log.pop(1)
            chat_log.append({"role": "user", "content": text})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
            max_tokens=150,
            n=1
        )
        bot_response = response.choices[0].message.content.strip("\n").strip()
        chat_log.append({"role": "assistant", "content": bot_response})

        data = {
            "bot_id": my_bot_id,
            "text": bot_response
        }
        response = requests.post(url, json=data)

    if '!' in data['text'].lower()[0]:
        bot_response = "bruh"
        if 'masjid' in data['text'].lower():
            bot_response = local_masjids
        elif 'halal' in data['text'].lower():
            bot_response = halal_options

        data = {
            "bot_id": my_bot_id,
            "text": bot_response
        }
        response = requests.post(url, json=data)

    return {'status': "OK"}

def announcement():

    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
        "text": jummah_announcment
    }
    response = requests.post(url, json=data)

if datetime.datetime.today().weekday() == 4:
    announcement()