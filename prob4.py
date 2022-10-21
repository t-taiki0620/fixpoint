# %% 設問4
import datetime
from ipaddress import ip_address, ip_network, ip_interface
str2datetime = lambda date: datetime.datetime.strptime(date, '%Y%m%d%H%M%S')
with open("log.txt", 'r')as f:
    log_file = [s.replace('\n','').split(',') for s in f.readlines()]
    
N = int(input())
log_dic = {}
address_list = []
for date, address, ping in log_file:
    if ip_interface(address).network not in log_dic.keys():
        log_dic[ip_interface(address).network] = {}
    
    if address not in log_dic[ip_interface(address).network].keys():
        if ping != '-':
            log_dic[ip_interface(address).network][address] = {'cnt_fail':0}
        else:
            log_dic[ip_interface(address).network][address] = {'cnt_fail':1}
    else:
        if ping == '-':
            if log_dic[ip_interface(address).network][address]['cnt_fail']==0:
                log_dic[ip_interface(address).network][address]['start']=date
            log_dic[ip_interface(address).network][address]['cnt_fail']+=1
        else:
            log_dic[ip_interface(address).network][address]['end']=date
            if log_dic[ip_interface(address).network][address]['cnt_fail'] >=N:
                print(f"{address} is timeout from {str2datetime(log_dic[ip_interface(address).network][address]['start'])} to {str2datetime(log_dic[ip_interface(address).network][address]['end'])}")
            start = []
            end = []
            cnt_fail =[]
            for v in log_dic[ip_interface(address).network].values():
                cnt_fail.append(v['cnt_fail'])
                try:
                    start.append(v['start'])
                    end.append(v['end'])
                except:
                    pass
            len_keys = log_dic[ip_interface(address).network]
            if (min(cnt_fail)>=N):
                print(f"{ip_interface(address).network} is broken from {str2datetime(min(start))} to {str2datetime(min(end))}")
            log_dic[ip_interface(address).network][address]['cnt_fail'] = 0
        
    
#%%