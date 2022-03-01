import os
import json
from twilio.rest import Client

cfg_file = open('ml_monitor.json', 'r')
cfg_dict = json.load(cfg_file)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = cfg_dict['account_side']
auth_token =  cfg_dict['account_token']
account_number = cfg_dict['account_number']
dest_number = cfg_dict['dest_number'] 

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=account_number,
                     to=dest_number
                 )

print(message.sid)

cfg_file.close()
