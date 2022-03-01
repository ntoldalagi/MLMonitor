import os
import json
from twilio.rest import Client

cfg_file = open('ml_monitor.json', 'r')
cfg_dict = json.load(cfg_file)
cfg_file.close()

account_sid = cfg_dict['account_side']
auth_token =  cfg_dict['account_token']
account_number = cfg_dict['account_number']
dest_number = cfg_dict['dest_number'] 

def epoch_update(epoch_num, model_name, metrics, first_epoch=None):
    client = Client(account_sid, auth_token)

    msg_body = '===== Epoch [{}] Complete ===== \n'.format(epoch_num)
    msg_body = msg_body.join('Model Name: {}\n\n'.format(model_name))
    msg_body = msg_body.join('Metrics:\n')
    for metric, metric_val in metrics:
        msg_body = msg_body.join('  {} ---- {}\n'.format(metric, float(metric_val)))

    message = client.messages \
                    .create(
                         body=msg_body,
                         from_=account_number,
                         to=dest_number
                     )
    
print(message.sid)

