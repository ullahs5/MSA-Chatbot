from urllib.request import urlopen
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hey", 200

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  if '.' in data['text'].lower()[0]:
      response_text = "yo"
      url = "https://api.groupme.com/v3/bots/post"
      data = {
          "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
          "text": response_text
      }
      response = requests.post(url, json=data)
      json = urlopen(response).read().decode()

  return {'status': "OK"}


