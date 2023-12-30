import datetime
import requests
from flask import Flask, request
from openai import OpenAI
import os
from messages import local_masjids, jummah_announcment, halal_options


AI_API_KEY = os.getenv('api_key')
client = OpenAI(api_key=AI_API_KEY)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hi", 200


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
            "bot_id": os.getenv('bot_id'),
            "text": bot_response
        }
        response = requests.post(url, json=data)

    if '!' in data['text'].lower()[0]:
        bot_response = "!masjid or !halal"
        if 'masjid' in data['text'].lower():
            bot_response = local_masjids
        elif 'halal' in data['text'].lower():
            bot_response = halal_options

        data = {
            "bot_id": os.getenv('bot_id'),
            "text": bot_response
        }
        response = requests.post(url, json=data)

    if "-" in data['text'].lower()[0]:
        numbering = data['text'][1:]
        ayah = requests.get(f"http://api.alquran.cloud/v1/ayah/{numbering}/en.yusufali").json()['data']['text']

        data = {
            "bot_id": os.getenv('bot_id'),
            "text": ayah
        }
        response = requests.post(url, json=data)


    return {'status': "OK"}


# def announcement():
#
#     url = "https://api.groupme.com/v3/bots/post"
#     data = {
#         "bot_id": os.getenv('bot_id'),
#         "text": jummah_announcment
#     }
#     response = requests.post(url, json=data)
#
# now = datetime.datetime.now()
# if now.hour == 1 and now.weekday() == 4:
#     announcement()