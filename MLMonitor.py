from twilio.rest import Client
import monitor_credentials as mc

import time

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

#report_epoch(3, 'model_1', total_epochs=22, loss=3.252523, accuracy=.135825, time=154.289)

class reporter:
    def __init__(self, total_steps):
        self.curr_avg_time = 0.0
        self.curr_steps = 0
        self.total_steps = 0

    def begin_timing(self):
        self.last_time = time.time()

    def time_step(self):
        self.curr_steps += 1
        time_delta = time.time() - self.last_time
        self.curr_avg_time = (self.curr_avg_time*(self.curr_steps-1) + time_delta)/(self.curr_steps)
        time_left = (self.total_steps - self.curr_steps) * self.curr_avg_time 
        print('EPOCH TIME [{}]s ESTIMATED TIME LEFT [{}]s'.format(self.curr_avg_time, time_left))



