from twilio.rest import Client
import os

account_sid = os.environ.get("Twilio_acc_sid")
auth_token = os.environ.get("Twlio_auth_token")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+923170031131'
)

print(message.sid)
