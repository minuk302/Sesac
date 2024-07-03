from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

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
        response_text = "하신 말씀을 반복하겠습니다." + text
        resp.say(response_text, voice='Polly.Seoyeon')
        # caller : request.values['Caller']
    else:
        # even this can be sent to LLM
        resp.say("잘 못들었어요. 다시 말씀해주시겠어요?", voice='Polly.Seoyeon')
    
    resp.append(create_speech_gather())
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)