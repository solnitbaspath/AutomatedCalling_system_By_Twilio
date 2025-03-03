
from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'AC868f6d7bcfb50ca71b92bc9ad78f066a'
auth_token = '210c6aa144acedd3e1db497f7d547db2'

client = Client(account_sid, auth_token)

call = client.calls.create(
    to='+919488402868',
    from_='+916382783822',
    url='https://handler.twilio.com/twiml/AC868f6d7bcfb50ca71b92bc9ad78f066a?' + urlencode({'Message': "Incident INC12345 assigned to you "})
)

print(call.sid)
call_sid = call.sid

time.sleep(60)

call = client.calls(call_sid).fetch()
print(call.status)

# List all the call logs from Twilio API
client = Client(account_sid, auth_token)
calls = client.calls.list(limit=20)

for record in calls:
    print(record.sid)

# Filter results for calls to a specific number with 'busy' status
calls = client.calls.list(status='busy', to='+919488402868', limit=20)

for record in calls:
    print(record.sid)

# # Check the status of a specific call using its SID
# call = client.calls('CAad384f2b2a0ca98ac8ac66211fe18334').fetch()
# print(call.status)
