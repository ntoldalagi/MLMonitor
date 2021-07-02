from twilio.rest import Client
import monitor_credentials as mc

def report_epoch(epoch):
    client = Client(mc.ACCOUNT_SID, mc.AUTH)
    msg = 'test message' 
    client.messages.create(mc.PERSONAL_NUMBER, from_=mc.TWILIO_NUMBER, body=msg)
report_epoch(1)
