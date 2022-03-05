# calc returns

import math
import sys

NUM_OF_CURRENCIES = 20

ONE_D_MSECS = 86400000

START_TIME_STAMP = 1364860800000
END_TIME_STAMP = 1640044800000

NUM_OF_DATA_POINTS = 3186
NUM_OF_RETURNS = 3185

prices = [[-1 for i in range(NUM_OF_DATA_POINTS)] for j in range(NUM_OF_CURRENCIES)]
returns = [[-1 for i in range(NUM_OF_RETURNS)] for j in range(NUM_OF_CURRENCIES)]
cur_name = []

f = open('C:/Users/kawam/Documents/Nomura/analysis/top20usd.csv', 'r')

data_list = f.readlines()

for i in range(len(data_list)):
    cur_name.append(data_list[i])

f.close()


for i in range(len(cur_name)):

    f = open('C:/Users/kawam/Documents/Nomura/archive/' + cur_name[i].rstrip('\r\n') + '.csv', 'r')    
    data_list = f.readlines()
    cur_day_end = START_TIME_STAMP

    p = 0
    cl = 0

    for j in range(1, len(data_list)):
        
        inputs = list(data_list[j].split(','))
        tm = int(inputs[0])
        last_cl = cl
        cl = float(inputs[2])

        if j == 1:
            while tm > cur_day_end:
                cur_day_end += ONE_D_MSECS
                p += 1
            
        if tm > cur_day_end and p <= NUM_OF_DATA_POINTS - 1:
            prices[i][p] = last_cl
            
            if p > 0:
                if prices[i][p - 1] != -1 and prices[i][p] != -1:
                    returns[i][p - 1] = math.log(prices[i][p] / prices[i][p - 1])
                    
            cur_day_end += ONE_D_MSECS
            p += 1
            cl = -1
            
    f.close()
    

# write returns into a file

f = open('C:/Users/kawam/Documents/Nomura/analysis/returns.csv', 'a')
fstr = 'TimeStamp,'

for i in range(NUM_OF_CURRENCIES):
    fstr += cur_name[i].rstrip('\r\n')
    
    if i != NUM_OF_CURRENCIES - 1:
        fstr += ','

f.write(fstr + '\n')
    
cur_day_end = START_TIME_STAMP    

for i in range(NUM_OF_RETURNS):
    
    cur_day_end += ONE_D_MSECS
    fstr = str(cur_day_end) + ','
    
    for j in range(NUM_OF_CURRENCIES):
        
        try:        
            fstr += str(returns[j][i])
        except:
            print('i = ' + str(i))
            print('j = ' + str(j))
            
        if j != NUM_OF_CURRENCIES - 1:

            fstr += ','
    
    f.write(fstr + '\n')

f.close()    
