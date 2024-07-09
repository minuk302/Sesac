from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import gemini_test

app = Flask(__name__)

# callBot keeps conversation history on memory. When server is down, history will be lost.
callbot = gemini_test.callBot()

def create_speech_gather():
    return Gather(
        input='speech', 
        action='/process_speech',
        action_on_empty_result=True,
        speech_timeout='1',
        language='ko-KR'
    )

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("안녕하세요. 무엇을 도와드릴까요?", voice='Polly.Seoyeon')
    resp.append(create_speech_gather())
    return str(resp)

@app.route("/process_speech", methods=['GET', 'POST'])
def process_speech():
    resp = VoiceResponse()
    if 'SpeechResult' in request.values:
        text = request.values['SpeechResult']
        number = request.values['Caller']
        response_text = callbot.chat(text, number)
        resp.say(response_text, voice='Polly.Seoyeon')
    else:
        # even this can be sent to LLM
        resp.say("잘 못들었어요. 다시 말씀해주시겠어요?", voice='Polly.Seoyeon')
    
    resp.append(create_speech_gather())
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)