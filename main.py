
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


print(types)

