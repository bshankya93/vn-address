import json

ftp = open('tinh_tp.json')
data = json.load(ftp)
ftp.close()
a = []
for i in data:
    a.append(data[i])
write = open('nk_tp.json', 'w')
write.write(json.dumps(a))
write.close()
print(a)