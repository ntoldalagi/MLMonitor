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
    msg_body = '{} First Epoch [{}]\n'.format(msg_body, first_epoch)
    msg_body = '{} Model Name: {}\n\n'.format(msg_body, model_name)
    msg_body = '{} Metrics:\n'.format(msg_body)
    for metric in metrics:
        msg_body = '{}  {} ---- {}\n'.format(msg_body, metric, float(metrics[metric]))
     
    message = client.messages \
                    .create(
                         body=msg_body,
                         from_=account_number,
                         to=dest_number
                     )

metric_dict = {}
metric_dict["loss"] = 1.2345
metric_dict["less2"] = 2.352
epoch_update(3, "new model", metric_dict, first_epoch=1)
