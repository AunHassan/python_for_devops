from twilio.rest import Client
import os
os.environ['Twilio_acc_sid'] = ("AC09115c383e9ce2d58e6e8c6a49152671")
os.environ['Twlio_auth_token'] = ("210667de29ce5c10155fc0c67d08b51c")
account_sid = os.environ.get("Twilio_acc_sid")
auth_token = os.environ.get("Twlio_auth_token")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+923170031131'
)

print(message.sid)