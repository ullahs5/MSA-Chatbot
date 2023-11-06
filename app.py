
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hey", 200

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'The Talker':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : '215bfbafb68c975c754166180e',
          'text'   : msg,
         }
  request = requests.post(url, json=data)
  json = urlopen(request).read().decode()

