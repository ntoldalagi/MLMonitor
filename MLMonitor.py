from twilio.rest import Client
import monitor_credentials as mc

def report_epoch(epoch, model_name, total_epochs=None, loss=None, accuracy=None, time=None, time_units='Secs'):
    msg = '{mn} UPDATE: \n'.format(mn=model_name.upper())
    msg += 'Epoch: {e}'.format(e=epoch)
    
    if total_epochs:
        msg += '    [{p}%]'.format(p=round(float(epoch)/total_epochs*100.0, 2))
    msg += '\n'

    if loss:
        loss = round(loss, 5)
        msg += 'Loss: {l}\n'.format(l=loss) 
    
    if accuracy:
        accuracy = round(accuracy, 5)
        msg += 'Acc: {a}\n'.format(a=accuracy) 

    if time:
        msg += 'Time: {t} {units}'.format(t=time, units=time_units) 

    client = Client(mc.ACCOUNT_SID, mc.AUTH)
    client.messages.create(mc.PERSONAL_NUMBER, from_=mc.TWILIO_NUMBER, body=msg)

report_epoch(3, 'model_1', total_epochs=22, loss=3.252523, accuracy=.135825, time=154.289)
