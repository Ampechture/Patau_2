# Developed by Kuznetsov.B - 50%, Odoevtsev.S - 25%, Makarov.A - 25%

from datetime import timedelta
import random
import math

azs = dict()
types = {}
cal = dict()
get_away = {}
oh = {}
trum = {}
time = 0
az = 0

with open('input.txt', 'r', encoding="utf8") as f1:
    q = f1.readlines()

with open('azs.txt', 'r', encoding="utf8") as f2:
    azd = f2.readlines()

for i in q:
    time += 1
    i = i.replace('\n', '').split(' ')
    types[time] = i

for col in azd:
    col_ = col.replace('\n', '').split(' ')
    azs[col_[0]] = col_[1:]


def time_fuel(fuel_amount, time_start):
    time_to_tuck = math.ceil(fuel_amount / 10) + random.randint(-1, 1)
    time_star = str(time_start).split(':')
    itog = timedelta(hours=int(time_star[0]), minutes=int(time_star[1])) + timedelta(minutes=time_to_tuck)
    if len((str(itog)[:-3].split(':'))[0]) == 1:
        itog = '0' + str(itog)[:-3]
        return itog
    else:
        return str(itog)[:-3]


for boops in types:
    cal[(types[boops])[0]] = ((types[boops][0]), (types[boops])[1], (types[boops])[2])

for new_time in cal:
    get_away[time_fuel(int(cal[new_time][1]), cal[new_time][0])] = cal[new_time]

for ara in get_away:
    oh[get_away[ara][0]] = ara


def colmun(benz):
    benz = str(benz).split('-')
    if int(benz[1]) == 80:
        return 1
    if int(benz[1]) == 92:
        return random.choice([2, 3])
    else:
        return 3


for run in oh:
    z = colmun(get_away[oh[run]][2])
    trum[run] = f'В {run} новый клиент:  {run} {get_away[oh[run]][2]} {get_away[oh[run]][1]} № {z}'
    trum[oh[
        run]] = f'В  {oh[run]}  клиент  {run} {get_away[oh[run]][2]} {get_away[oh[run]][1]} ' \
                f'заправил свой автомобиль и покинул АЗС'



list_d = list(trum.items())
list_d.sort()
for ites in list_d:
    print(ites[1])
