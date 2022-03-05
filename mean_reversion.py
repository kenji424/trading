# mean reversion

import sys
import math

LAST_1Y_TIME_STAMP = 1608508800000
HOLDING_PERIOD = 3

cur = ['btcusd', 'ethusd', 'ustusd', 'xrpusd', 'ltcusd', 'solusd', 'eosusd', 'dotusd', 'adausd', 'iotusd',
       'uniusd', 'xtzusd', 'trxusd', 'omgusd', 'zecusd', 'etcusd', 'udcusd', 'dshusd', 'xlmusd', 'neousd']

pr = [0.0] * 4
trade_i = 0

init_long_pr = 0.0
init_short_pr = 0.0

long_init_pr = 0.0
short_init_pr = 0.0

b_long = False
b_short = False

output1 = 'currency'
output2 = 'long_threshold'
output3 = 'long_trades'
output4 = 'long_wins'
output5 = 'long_total_percent'
output6 = 'long_average'

output7 = 'currency'
output8 = 'short_threshold'
output9 = 'short_trades'
output10 = 'short_wins'
output11 = 'short_total_percent'
output12 = 'short_average'

for k in range(len(cur)):

    file = cur[k] + '.csv'     
    f = open('C:/Users/kawam/Documents/Nomura/archive/' + file, 'r')
    data_list = f.readlines()
    f.close()

    long_threshold = -0.002
    short_threshold = 0.002    
    
    output1 = 'currency'
    output2 = 'long_threshold'
    output3 = 'long_trades'
    output4 = 'long_wins'
    output5 = 'long_total_percent'
    output6 = 'long_average'
    
    output7 = 'currency'
    output8 = 'short_threshold'
    output9 = 'short_trades'
    output10 = 'short_wins'
    output11 = 'short_total_percent'
    output12 = 'short_average'
    
    for j in range(6):
    
        long_threshold -= 0.001
        short_threshold += 0.001
    
        long_trades = 0
        short_trades = 0
        
        long_wins = 0
        short_wins = 0
    
        long_total_percent = 0.0
        short_total_percent = 0.0
    
        for i in range(1, len(data_list)):
            
            inputs = list(data_list[i].split(','))
            
            if i <= 4:
                pr[i - 1] = float(inputs[2])
        
            else:
                bench_pr = 0.4 * pr[3] + 0.3 * pr[2] + 0.2 * pr[1] + 0.1 * pr[0]
        
                tm = int(inputs[0])
                cl = float(inputs[2])
                
                if tm < LAST_1Y_TIME_STAMP:
                
                    # long liquidate trade
                    if i == trade_i + HOLDING_PERIOD and b_long == True:
                        long_trades += 1
                        
                        if cl > long_init_pr:
                            long_wins += 1
                            
                        long_total_percent += math.log(cl / long_init_pr)                    
                        b_long = False
           
                    # short liquidate trade
                    if i == trade_i + HOLDING_PERIOD and b_short == True:
                        short_trades += 1
                                    
                        if cl < short_init_pr:
                            short_wins += 1
                            
                        short_total_percent += math.log(short_init_pr / cl)                    
                        b_short = False
            
                    # long initiate trade        
                    if math.log(cl / bench_pr) < long_threshold and b_long == False:
                        trade_i = i
                        long_init_pr = cl
                        b_long = True
                                    
                    # short initiate trade        
                    if math.log(cl / bench_pr) > short_threshold and b_short == False:
                        trade_i = i
                        short_init_pr = cl
                        b_short = True
                                            
                    pr[0] = pr[1]
                    pr[1] = pr[2]
                    pr[2] = pr[3]
                    pr[3] = cl
    
        output1 += ',' + cur[k]
        output2 += ',' + str(long_threshold)
        output3 += ',' + str(long_trades)
        output4 += ',' + str(long_wins)
        output5 += ',' + str(long_total_percent)
        if long_trades != 0:
            output6 += ',' + str(long_total_percent / float(long_trades))
        else:
            output6 += ',0'
        
        output7 += ',' + cur[k]
        output8 += ',' + str(short_threshold)
        output9 += ',' + str(short_trades)
        output10 += ',' + str(short_wins)
        output11 += ',' + str(short_total_percent)
        if short_trades != 0:
            output12 += ',' + str(short_total_percent / float(short_trades))
        else:
            output12 += ',0'
    
    f = open('C:/Users/kawam/Documents/Nomura/mean_reversion/mean_reversion_summary.csv', 'a')
    
    f.write(output1 + '\n')
    f.write(output2 + '\n')
    f.write(output3 + '\n')
    f.write(output4 + '\n')
    f.write(output5 + '\n')
    f.write(output6 + '\n')
    f.write('\n')
    f.write(output7 + '\n')
    f.write(output8 + '\n')
    f.write(output9 + '\n')
    f.write(output10 + '\n')
    f.write(output11 + '\n')
    f.write(output12 + '\n')
    f.write('\n')
    
    f.close()
