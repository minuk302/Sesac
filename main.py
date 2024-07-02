# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import configparser

config = configparser.ConfigParser()
config.read('secret.ini')

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config['DEFAULT']["TWILIO_ACCOUNT_SID"]
auth_token = config['DEFAULT']["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to="+15558675310",
    from_=config['DEFAULT']["TWILIO_PHONE_NUMBER"],
)

print(call.sid)