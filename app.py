from urllib.request import urlopen
import requests
from flask import Flask, request
from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hello", 200



chat_log = []

@app.route('/', methods=['POST'])
def webhook():
    global chat_log
    data = request.get_json()
    url = "https://api.groupme.com/v3/bots/post"

    if '.' in data['text'].lower()[0]:
        text = data['text'].lower()[1:]
        text = "You're a VERY CHILL and relaxed MUSLIM who BANTERS and JOKES, ONLY SHORT responses: " + text
        chat_log.append({"role": "user", "content": text})
        if len(chat_log) > 6:
            chat_log = chat_log[-6:]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
            max_tokens=150
        )
        bot_response = response.choices[0].message.content.strip("\n").strip()
        chat_log.append({"role": "assistant", "content": bot_response})

        data = {
            "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
            "text": bot_response + len(chat_log)
        }
        if len(chat_log) > 6:
            chat_log.clear()

        response = requests.post(url, json=data)

    return {'status': "OK"}






# client.api_key = API_KEY

# def chat(text):
#     global chat_log
#     user_message = text
#     chat_log.append({"role": "user", "content": user_message})
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=chat_log,
#         max_tokens=150
#     )
#     bot_response = response.choices[0].message.content.strip("\n").strip()
#     chat_log.append({"role": "assistant", "content": bot_response})
#     return bot_response
