string = input().split(" ")
number = []
volume_all = []
for i in string:
    volume_all.append(int(i))

premia = 200
max_volume = 0
for i in string:
    volume = int(i)
    zp = 200 #basa
    #print(volume)
    if 0 < volume < 500:
        zp *= 1.03
    elif 500 <= volume <= 1000:
        zp *= 1.05
    elif volume > 1000:
        zp *= 1.08
    number.append(zp)
    #print(number)

count_max = 0
for i in string:
    max_volume = max(volume_all)
    if max_volume == int(i):
        count_max += 1
print("количество масимальных значений: ",count_max)

k = 0
for i in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(i):
        print("макс обьем", i)
        number[k] += premia / count_max
    k += 1
print(number)

