import random
import math

hours = 0
t = {}
azs = dict()
count = {}
types = {}
cal = dict()
turn = dict()
strt = dict()
out = dict()

time = 0
az = 0

with open('input.txt', 'r', encoding="utf8") as f1:
    q = f1.readlines()

with open('azs.txt', 'r', encoding="utf8") as f2:
    azs = f2.readlines()

for i in q:
    time += 1
    i = i.replace('\n', '').split(' ')
    types[time] = i

for a in azs:
    az += 1
    a = a.replace("\n", "").split(' ')
    print(a)
    n = int(a[0])
    o = int(a[1])
    t = a[2]
    azs[n] = (t, o)

print(azs)
# print(types)

def time_fuel(fuel_amount, time_start):
    fuel_amount = math.ceil(fuel_amount)
    time_to_tuck = fuel_amount / 10 + random.randint(-1, 1)
    total_time = time_start + time_to_tuck
    return (total_time)


def slv(types):  # создаем словарь по времени
    for boops in types:
        cal[(types[boops])[0]] = ((types[boops])[1], (types[boops])[2])

    for pineapple in cal:
        "shaitan = time_fuel((cal[pineapple])[1], pineapple)"
        strt[pineapple] = (pineapple, (cal[pineapple])[1], (cal[pineapple])[0])

    print(strt)

    for ta in cal:
        turn[ta] = (ta, (cal[ta])[1])

    for el in types:
        print(el)
        out[el] = tuple(cal[in_], in_[in_])


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
        if len(minutes) < 2 and len(hours) < 2:
            minutes = '0' + minutes
            hours = '0' + hours
        elif len(minutes) < 2:
            minutes = '0' + minutes
        elif len(hours) < 2:
            hours = str(hours)
            hours = '0' + hours
        all_keys_time = str(hours) + ':' + str(minutes)

        # print(all_keys_time)
        minutes = int(minutes)
        hours = int(hours)

slv(types)
tablo(cal)
