from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC868f6d7bcfb50ca71b92bc9ad78f066a'
auth_token = '210c6aa144acedd3e1db497f7d547db2'
client = Client(account_sid, auth_token)

def makecall():
    call = client.calls.create(
        to ='+916382783822',
        from_='+12512741976',
        # url='https://api.twilio.com/2010-04-01/Accounts/AC868f6d7bcfb50ca71b92bc9ad78f066a/Calls.json' + urlencode(
        #     {'Message': "hello"})
        url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770' + urlencode( {'Message': "hello"})
    )
    print(call.sid)
    call_sid = call.sid

    time.sleep(30)

    call = client.calls(call_sid).fetch()
    print(call.status)

def sendsms(msg):
    message = client.messages \
        .create(
        body=msg,
        from_='+12512741976',
        to ='+916382783822'
    )

    print(message.sid)

print("exceuted succesfully !!!!")