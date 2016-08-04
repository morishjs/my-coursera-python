import re

f = open("regex_sum_300257.txt","r")
lines = f.readlines()
sum = 0

for line in lines:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for number in x:
        sum += int(number)


print sum
f.close()