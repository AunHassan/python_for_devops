from twilio.rest import Client
from key import account_sid,auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+923170031131'
)

print(message.sid)