# %% 設問2
import datetime

str2datetime = lambda date: datetime.datetime.strptime(date, '%Y%m%d%H%M%S')
with open("log.txt", 'r')as f:
    log_file = [s.replace('\n','').split(',') for s in f.readlines()]
    
N = int(input())
log_dic = {}
for date, address, ping in log_file:
    if address not in log_dic.keys():
        if ping == '-':
            log_dic[address] = {'cnt_fail':1}
        else:
            log_dic[address] = {'cnt_fail':0}       
    else:
        if ping == '-':
            if log_dic[address]['cnt_fail']==0:
                log_dic[address]['start']=date
            log_dic[address]['cnt_fail']+=1
        else:
            log_dic[address]['end']=date
            if log_dic[address]['cnt_fail'] >=N:
                print(f"{address} is timeout from {str2datetime(log_dic[address]['start'])} to {str2datetime(log_dic[address]['end'])}")
                log_dic[address]['cnt_fail'] = 0
#%% 