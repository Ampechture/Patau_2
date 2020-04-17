import random


t ={}
count = {}
types = {}
time = 0
with open('input.txt') as f1:
    q = f1.readlines()

for i in q:
    time +=1
    i = i.replace('\n','').split(' ')
    types[time] = i

def time(count_oil, income_time):
    z = [0, 1, -1]
    r = str(income_time).split(':')
    hour = r[0]
    minut = r[1]
    total_time = round(count_oil/10)
    minut =+ total_time + random.choice(z)
    if minut >= 60:
        hour +=1
        minut -=60
        return str(f'{hour}:{minut}')
    else:
        return str(f'{hour}:{minut}')





print(time(2, '13:45'))