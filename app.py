
# import json
#
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
#
# import requests
# from flask import Flask, request
#
# app = Flask(__name__)
#
# @app.route("/", methods=['GET'])
# def hello():
#     return "hey", 200
#
# @app.route('/', methods=['POST'])
# def webhook():
#   data = request.get_json()
#
#   # We don't want to reply to ourselves!
#   if data['name'] != 'The Talker':
#     msg = '{}, you sent "{}".'.format(data['name'], data['text'])
#     send_message(msg)
#
#   return "ok", 200
#
# def send_message(msg):
#   url  = 'https://api.groupme.com/v3/groups/97130171/messages?token=ytitIf5Eb3KKfHcDuT20MGmaTpMEyCBR2CrGmFAd'
#
#   data = {
#           'bot_id' : '7a68edb9635828c387afad07d7',
#           'text'   : msg,
#          }
#   request = requests.post(url, json=data)
#   json = urlopen(request).read().decode()

import requests


from fastapi import FastAPI, Request

#bot_token = "7a68edb9635828c387afad07d7"
app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    data = await request.json()

    if '.' in data['text'].lower()[0]:
        response_text = "yo"
        url = "https://api.groupme.com/v3/groups/97130171/messages?token=ytitIf5Eb3KKfHcDuT20MGmaTpMEyCBR2CrGmFAd"
        data = {
            "bot_id": "7a68edb9635828c387afad07d7",
            "text": response_text
        }
        response = requests.post(url, json=data)
        print(response.status_code)

    return {'status': "OK"}

@app.get("/")
def hello():
    return "hey", 200

