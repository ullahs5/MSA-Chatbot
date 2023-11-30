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



# chat_log = [{"role": "system", "content": "You have MUSLIM etiquette, SHORT comedic responses:"}]
#chat_log = [{"role": "system", "content": "Mimic rude and sarcastic, SHORT responses: "}]
chat_log = [{"role": "system", "content": "You're very funny and sarcastic, SHORT responses: "}]

@app.route('/', methods=['POST'])
def webhook():
    global chat_log
    data = request.get_json()
    url = "https://api.groupme.com/v3/bots/post"

    # if '.' in data['text'].lower()[0]:
    #     text = data['text'].lower()[1:]
    #     if len(chat_log) < 4:
    #         chat_log.append({"role": "user", "content": text})
    #     else:
    #         chat_log.pop(1)
    #         chat_log.pop(1)
    #         chat_log.append({"role": "user", "content": text})
    #
    #     response = client.chat.completions.create(
    #         model="gpt-3.5-turbo",
    #         messages=chat_log,
    #         max_tokens=150,
    #         n=1
    #     )
    #     bot_response = response.choices[0].message.content.strip("\n").strip()
    #     chat_log.append({"role": "assistant", "content": bot_response})
    #
    #     data = {
    #         "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
    #         "text": bot_response
    #     }
    if data['name'] != 'Saif UIlah':
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
            "bot_id": "2c2d597644b8b85a57bd27b0ba",
            "text": bot_response
        }

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
