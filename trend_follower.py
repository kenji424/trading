# trend follower

import sys
import math


LAST_2Y_TIME_STAMP = 1576972800000
LAST_1Y_TIME_STAMP = 1608508800000


cur1 = 'btcusd'
cur2 = 'ethusd'

tm = []
pr1 = []
pr2 = []

file = cur1 + '-' + cur2 + '.csv'

f = open('C:/Users/kawam/Documents/Nomura/pairs/' + file, 'r')

data_list = f.readlines()

for i in range(1, len(data_list)):
    inputs = list(data_list[i].split(','))
    tm.append(int(inputs[0]))
    pr1.append(float(inputs[1]))
    pr2.append(float(inputs[2]))
    
f.close()

long_trades = 0
long_wins = 0
long_total_percent = 0.0

short_trades = 0
short_wins = 0
short_total_percent = 0.0


output1 = 'cur1_up'
output2 = 'cur2_up'
output3 = 'long_trades'
output4 = 'long_wins'
output5 = 'long_total_percent'
output6 = 'long_average_percent'
output7 = 'cur1_down'
output8 = 'cur2_down'
output9 = 'short_trades'
output10 = 'short_wins'
output11 = 'short_total_percent'
output12 = 'short_average_percent'


cur1_up = 0.002
cur1_down = -0.002


for m in range(5):

    print('m = ' + str(m))
    
    cur1_up += 0.001
    cur1_down -= 0.001

    cur2_up = -0.001
    cur2_down = 0.001
    
    for n in range(3):
        
        print('n = ' + str(n))
        
        cur2_up += 0.001
        cur2_down -= 0.001

        long_trades = 0
        long_wins = 0
        long_total_percent = 0.0

        short_trades = 0
        short_wins = 0
        short_total_percent = 0.0

        for i in range(1, len(tm) - 1):
            
            if tm[i] < LAST_1Y_TIME_STAMP and tm[i] >= LAST_2Y_TIME_STAMP:
            
                if math.log(pr1[i] / pr1[i - 1]) > cur1_up and math.log(pr2[i] / pr2[i - 1]) < cur2_up:
            
                    '''
                    print(tm[i])
                    print('Buy ' + cur2 + ' @ ' + str(pr2[i]))
                    print(tm[i + 1])
                    print('Sell ' + cur2 + ' @ ' + str(pr2[i + 1]))
                    print()
                    '''
                    
                    long_trades += 1
                    
                    if pr2[i + 1] > pr2[i]:
                        long_wins += 1
                    
                    long_total_percent += math.log(pr2[i + 1] / pr2[i])
                    
                elif math.log(pr1[i] / pr1[i - 1]) < cur1_down and math.log(pr2[i] / pr2[i - 1]) > cur2_down:
        
                    '''
                    print(tm[i])
                    print('Sell ' + cur2 + ' @ ' + str(pr2[i]))
                    print(tm[i + 1])
                    print('Buy ' + cur2 + ' @ ' + str(pr2[i + 1]))
                    print()
                    '''
                    
                    short_trades += 1
                    
                    if pr2[i + 1] < pr2[i]:
                        short_wins += 1
                        
                    short_total_percent += math.log(pr2[i] / pr2[i + 1])
        

        output1 += ',' + str(cur1_up)
        output2 += ',' + str(cur2_up)
        output3 += ',' + str(long_trades)
        output4 += ',' + str(long_wins)
        output5 += ',' + str(long_total_percent)
        output6 += ',' + str(long_total_percent / float(long_trades))
        output7 += ',' + str(cur1_down)
        output8 += ',' + str(cur2_down)
        output9 += ',' + str(short_trades)
        output10 += ',' + str(short_wins)
        output11 += ',' + str(short_total_percent)
        output12 += ',' + str(short_total_percent / float(short_trades))




file_out = cur1 + '-' + cur2 + 'trend_follow.csv'

f = open('C:/Users/kawam/Documents/Nomura/trend_follow/' + file_out, 'a')

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

f.close()




'''
print('cur1_up')
print('cur2_up')
print('long_trades = ' + str(long_trades))
print('long_wins = ' + str(long_wins))
print('long_total_percent = ' + str(long_total_percent))
print('long_average_percent = ' + str(long_total_percent / float(long_trades)))

print()

print('cur1_down')
print('cur2_down')
print('short_trades = ' + str(short_trades))
print('short_wins = ' + str(short_wins))
print('short_total_percent = ' + str(short_total_percent))
print('short_average_percent = ' + str(short_total_percent / float(short_trades)))
'''












