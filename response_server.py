from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Hi, Gabriela. You look so cute!", voice='Polly.Amy')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)