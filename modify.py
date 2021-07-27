import json
from os import listdir
from os.path import isfile, join
mypath = 'xa-phuong'
outpath = 'nk-xp'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    fj = open(mypath+'/'+file)

    print(file)
    data = json.load(fj)
    a = []
    for i in data:
        a.append(data[i])
    oj = open(outpath + '/' + file, 'w')
    oj.write(json.dumps(a))
    oj.close()