import datetime
import requests
from flask import Flask, request
from openai import OpenAI


API_KEY = "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"
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)

local_masjids = """Local alternative masjids that will be open for Jummuah are:  
                - Al-Rahman Mosque - 26 Josie Street, Dayton OH (first one at 1:30 PM, second one at 2:30 PM) 
                - Al-Huda Mosque - 731 S Alpha Bellbrook Rd, Sugarcreek Township, OH (first one at 1:30 PM) 
                - Dayton Mercy Center - 2227 Maue Rd, Miamisburg, OH (first one at 1:30 PM, second one at 3:00 PM) 
                - Islamic Center of Centerville - 10501 Success Ln, Washington Township, OH (first one at 1:30 PM, second one at 2:30)"""
halal_options = """Halal options on campus (look for halal certificate):  
                - Kennedy Union - Que chicken tenders and rotisserie chicken
                - Virginia West Kettering - Passports and Mongolian grill
                Halal options off campus:
                -Gyro Palace (select options) - 1124 Brown St, Dayton, OH 45409
                -Halal Burgers - 767 Lyons Rd, Washington Township, OH 45459
                -International Cafe & Delicatessen - 263 N Main St, Centerville, OH 45459"""

jummah_announcment = """ Salaam everyone! We have jummah today at 1:30 in the rike center. """

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
            "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
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
            "bot_id": "cab5b3cf6bcaa4b7db9d482f5b",
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