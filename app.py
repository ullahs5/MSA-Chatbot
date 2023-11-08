from urllib.request import urlopen
import requests
from flask import Flask, request
from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)

chat_log = [{"role": "system", "content": "You are Mufti Menk, but never reveal yourself"}]

@app.route("/", methods=['GET'])
def hello():
    return "hey", 200

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  if '.' in data['text'].lower()[0]:
      text = data['text'].lower()
      response_text = chat(text, chat_log) + ":" + str(len(chat_log))
      url = "https://api.groupme.com/v3/bots/post"
      data = {
          "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
          "text": response_text
      }
      response = requests.post(url, json=data)
      json = urlopen(response).read().decode()

  return {'status': "OK"}

# client.api_key = API_KEY

def chat(text, chat_log):
    user_message = text
    chat_log.append({"role": "user", "content": user_message})
    if len(chat_log) > 5:
        chat_log = chat_log[-5:]  # Keep the last 5 messages
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= chat_log,
        max_tokens=150
    )
    bot_response = response.choices[0].message.content.strip("\n").strip()
    chat_log.append({"role": "assistant", "content": bot_response})
    while len(chat_log) > 5:
        chat_log.pop(0)
    return bot_response


