import requests
from flask import Flask, request
from openai import OpenAI
from config import api_key, my_bot_id


API_KEY = api_key
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hello", 200

local_masjids = """Local alternative masjids that will be open for Jummuah are:  
- Al-Rahman Mosque - 26 Josie Street, Dayton OH (first one at 1:30 PM, second one at 2:30 PM) 
- Al-Huda Mosque - 731 S Alpha Bellbrook Rd, Sugarcreek Township, OH (first one at 1:30 PM) 
- Dayton Mercy Center - 2227 Maue Rd, Miamisburg, OH (first one at 1:30 PM, second one at 3:00 PM) 
- Islamic Center of Centerville - 10501 Success Ln, Washington Township, OH (first one at 1:30 PM, second one at 2:30)"""

chat_log = [{"role": "system", "content": "You're witty, short responses: "}]

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
        bot_response = ""
        if 'local masjids' in data['text'].lower():
            bot_response = local_masjids

        data = {
            "bot_id": my_bot_id,
            "text": bot_response
        }
        response = requests.post(url, json=data)

    return {'status': "OK"}
