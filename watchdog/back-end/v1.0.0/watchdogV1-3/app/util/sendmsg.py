from twilio.rest import Client

def send(num, msg):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC492a1a3283e499614391f3aa247b26be'
    auth_token = 'fda84c6698b9e0d7990f5b813a1465d7'
    client = Client(account_sid, auth_token)

    message = client.messages .create(
        body=msg,
        from_='+12029492612',
        to=num
    )