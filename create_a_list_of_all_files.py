# create a list of all files

import glob

files = glob.glob('C:/Users/kawam/Documents/Nomura/archive/*')
f = open('C:/Users/kawam/Documents/Nomura/usd-list.csv', 'a')

for file in files:
    
    if 'usd.' in file:
        f.write(file[40:] + '\n')

f.close()
