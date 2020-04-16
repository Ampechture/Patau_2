import random
import math

hours = 0
t ={}
count = {}
types = {}
time = 0
with open('input.txt', 'r', encoding="utf8") as f1:
    q = f1.readlines()

for i in q:
    time += 1
    i = i.replace('\n', '').split(' ')
    types[time] = i


print(types)
def time_fuel(fuel_amount, time_start):
    fuel_amount = math.ceil(fuel_amount)
    time_to_tuck = fuel_amount / 10 + random.randint(-1,1)
    total_time = time_start + time_to_tuck
    return(total_time)

minutes = 0
hours = 0

while hours != 24:
    while minutes != 60:
        minutes += 1
        if minutes == 60:
            hours += 1
            minutes = 0
            break
        minutes = str(minutes)
        hours = str(hours)
        if len(minutes)< 2 and len(hours) < 2:
            minutes = '0' + minutes
            hours = '0' + hours
        elif len(minutes) < 2:
            minutes = '0' + minutes
        elif len(hours) < 2:
            hours = str(hours)
            hours = '0' + hours
        all_keys_time = str(hours) + ':' + str(minutes)
        print(all_keys_time)
        minutes = int(minutes)
        hours = int(hours)

