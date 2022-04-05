import sys
import time
name= sys.argv[1]
file1 = open(name, "r")
fl = 0
t0 = time.time()
while True:
    line = file1.readline()

    if line=='':
        break
    line = int(line)
    if fl == 0:
        mx = line
        count = 1
        fl = 1
        continue
    if line > mx:
        mx = line
        count = 1
        continue
    if line == mx:
        count += 1

file1.close

print(f'maximal element is {mx} amount is {count}')
print(time.time()-t0)