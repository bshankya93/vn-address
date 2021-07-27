import json
from os import listdir
from os.path import isfile, join
mypath = 'quan-huyen'
outpath = 'nk-qh'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    fj = open(mypath+'/'+file)

    print(file)
    data = json.load(fj)
    # a = [{'code': 0, 'name': 'Chọn QH'}]
    a = []
    for i in data:
        a.append(data[i])
    oj = open(outpath + '/' + file, 'w')
    oj.write(json.dumps(a))
    oj.close()