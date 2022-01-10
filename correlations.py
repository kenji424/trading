# correlations

import pandas as pd
import numpy as np
import sys


NUM_OF_CURRENCIES = 20
NUM_OF_RETURNS = 3185

CORREL_RETURNS = 2820

cur_name = []

f = open('C:/Users/kawam/Documents/Nomura/analysis/top20usd.csv', 'r')

data_list = f.readlines()

for i in range(len(data_list)):
    cur_name.append(data_list[i].rstrip('\r\n'))

f.close()


returns = [[-1 for i in range(NUM_OF_RETURNS)] for j in range(NUM_OF_CURRENCIES)]

f = open('C:/Users/kawam/Documents/Nomura/analysis/returns.csv', 'r')

data_list = f.readlines()

for i in range(1, len(data_list)):
    inputs = list(data_list[i].split(','))

    for j in range(len(NUM_OF_CURRENCIES)):        
        returns[j][i - 1] = float(inputs[j + 1])


f.close()


correlations = [[1 for i in range(NUM_OF_CURRENCIES)] for j in range(NUM_OF_RETURNS)]

returns1 = []
returns2 = []

for i in range(NUM_OF_CURRENCIES - 1):
    
    for j in range(i + 1, NUM_OF_CURRENCIES):
        
        for k in range(CORREL_RETURNS):
            
            if returns[i][k] != -1 and returns[j][k] != -1:
                
                returns1.append(returns[i][k])
                returns2.append(returns[j][k])
        
        s1 = pd.Series(returns1)
        s2 = pd.Series(returns2)

        corr = s1.corr(s2)
        
        correlations[i][j] = corr
        correlations[j][i] = corr
        

f = open('C:/Users/kawam/Documents/Nomura/analysis/correlations.csv', 'a')

for i in range(NUM_OF_CURRENCIES + 1):

    output = ''
    
    if i == 0:

        output += ','
                
        for j in range(NUM_OF_CURRENCIES):
            output += cur_name[j]
            
            if j != NUM_OF_CURRENCIES - 1:
                output += ','
        
    else:
        
        output += cur_name[i - 1] + ','
        
        for j in range(NUM_OF_CURRENCIES):
            
            output += str(correlations[i - 1][j])
            
            if j != NUM_OF_CURRENCIES - 1:
                output += ','
                
    f.write(output + '\n')
        
f.close()
        
        
        


























