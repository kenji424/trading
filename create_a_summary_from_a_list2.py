# create a summary from a list

LAST_1Y_TIME_STAMP = 1608508800000

# open a currency list file
f = open('C:/Users/kawam/Documents/Nomura/analysis/usd-list.csv', 'r')
file_list = f.readlines()
f.close()

cur_name = []
start_time = []
end_time = []

days = []

open_price = []
close_price = []
high_price = []
low_price = []

trade_values = []
daily_trade_values = []

trade_values_1Y = []
daily_trade_values_1Y = []


for i in range(len(file_list)):
#for i in range(10):

    cur_name.append(file_list[i][:len(file_list[i]) - 5])
    
    f = open('C:/Users/kawam/Documents/Nomura/archive/' + file_list[i].rstrip('\r\n'), 'r')
    
    data_list = f.readlines()
    
    trade_value = 0.0
    trade_value_1Y = 0.0
    
    high = 0.0
    low = 10**20
    
    for j in range(1, len(data_list)):
        
        inputs = list(data_list[j].split(','))
        
        tm = int(inputs[0])
        op = float(inputs[1])
        cl = float(inputs[2])
        hi = float(inputs[3])
        lo = float(inputs[4])
        vol = float(inputs[5])
        
        if j == 1:
            st = tm
            start_time.append(tm)
            open_price.append(op)
            
        if hi > high:
            high = hi
        
        if lo < low:
            low = lo
        
        trade_value += cl * vol
        
        if tm >= LAST_1Y_TIME_STAMP:
            trade_value_1Y += cl * vol
        

    end_time.append(tm)
    
    day = int((tm - st) / 86400000)
    
    days.append(day)
    
    close_price.append(cl)
    high_price.append(high)
    low_price.append(low)

    trade_values.append(trade_value)
    daily_trade_values.append(trade_value / day)
    
    trade_values_1Y.append(trade_value_1Y)
    daily_trade_values_1Y.append(trade_value_1Y / 365.0)
    


# put data into a summary file
    
f = open('C:/Users/kawam/Documents/Nomura/analysis/usd-Summary.csv', 'w')

f.write('Currency,StartTime,EndTime,Days,Open,Close,High,Low,TradeValue,DailyTradeValue,TradeValue1Y,DailyTradeValue1Y\n')

for i in range(len(file_list)):
#for i in range(10):
     
    f.write(cur_name[i] + ',' + str(start_time[i]) + ',' + str(end_time[i]) + ',' + 
            str(days[i]) + ',' + str(open_price[i]) + ',' + str(close_price[i]) + ',' + 
            str(high_price[i]) + ',' + str(low_price[i]) + ',' + str(trade_values[i]) + ',' + 
            str(daily_trade_values[i]) + ',' + str(trade_values_1Y[i]) + ',' + str(daily_trade_values_1Y[i]) + ',' + '\n')

f.close()

            







