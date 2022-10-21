#%% 設問1
from cmath import log
import datetime

str2datetime = lambda date: datetime.datetime.strptime(date, '%Y%m%d%H%M%S')
with open("log.txt", 'r')as f:
    log_file = [s.replace('\n','').split(',') for s in f.readlines()]

log_dic = {}
for date, address, ping in log_file:
    if address not in log_dic.keys():
        if ping == '-' :
            log_dic[address] = {'start':date}
    else:
        if ping != '-':
            log_dic[address]['end'] = date

for address in log_dic.keys():
    print(f"{address} is timeout from {str2datetime(log_dic[address]['start'])} to {str2datetime(log_dic[address]['end'])}")
# %%