from twilio.rest import TwilioRestClient

account_sid = "{{ ACca427cbc84148d2a467ab5b4cd80dda3 }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ 948ff29c972390ed3e8b473b57311152 }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+917715895075",    # Replace with your phone number
    from_="+12406502492") # Replace with your Twilio number

print(message.sid)
