# %%設問3
import datetime

str2datetime = lambda date: datetime.datetime.strptime(date, '%Y%m%d%H%M%S')

with open("log.txt", 'r')as f:
    log_file = [s.replace('\n','').split(',') for s in f.readlines()]
    
N, m, t = [int(x) for x in input().split()]
log_dic = {}
for date, address, ping in log_file:
    if address not in log_dic.keys():
        log_dic[address] = {'date':[date], 'cnt_fail':0}
        if ping != '-':
            log_dic[address]['ping'] = [int(ping)]
    else:
        if ping == '-':
            if log_dic[address]['cnt_fail']==0:
                log_dic[address]['start']=date
            log_dic[address]['date']=[]
            log_dic[address]['ping']=[]
            log_dic[address]['cnt_fail']+=1
        else:
            log_dic[address]['date'].append(date)
            log_dic[address]['ping'].append(int(ping))
            log_dic[address]['end']=date
            if log_dic[address]['cnt_fail'] >=N:
                print(f"{address} is timeout from {str2datetime(log_dic[address]['start'])} to {str2datetime(log_dic[address]['end'])}")
                log_dic[address]['cnt_fail'] = 0
            
            if len(log_dic[address]['ping']) > m:
                log_dic[address]['date'].pop(0)
                log_dic[address]['ping'].pop(0)
            if len(log_dic[address]['ping'])==m and sum(log_dic[address]['ping'])/m > t:
                print(f"{address} is overload from {str2datetime(log_dic[address]['date'][0])} to {str2datetime(log_dic[address]['date'][-1])}")
# %%
