import json
from os import listdir
from os.path import isfile, join
f = open('tinh_tp.json')
data = json.load(f)
a = []
for i in range(1,96):
    for j in data:
        if(int(data[j]['code']) == i):
            a.append(data[j])

oj = open('tp_sorted.json', 'w')
oj.write(json.dumps(a))
oj.close()