string = input().split(" ")
base = 200 # базовая ставка 200$
percent = 0
premiya = 0
status = 0
if (int(string[0]) > int(string[1]) > int(string[2])
        or int(string[0]) > int(string[2]) > int(string[1])):
    status = 0
    print("премия начислится менджеру №: ", status)
if (int(string[1]) > int(string[2]) > int(string[0])
        or int(string[1]) > int(string[0]) > int(string[2])):
    status = 1
    print("премия начислится менджеру №: ", status)
if (int(string[2]) > int(string[1]) > int(string[0])
        or int(string[2]) > int(string[0]) > int(string[1])):
    status = 2
    print("премия начислится менджеру №: ", status)


k = 0
for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif 500 <= zp < 1000:
        percent = 0.05
    elif zp >= 1000:
        percent = 0.08
    #print(k)

    if k == status:
        premiya += 200
        print("Менеджер №: ",k+1,", ", base * (1 + percent) + premiya)
    else:
        print("Менеджер №: ", k+1, ", ", base * (1 + percent))
    k += 1


# zp_all = []
# for i in string:
#     zp_all.append(int(i))
# zp_all.sort(reverse=True)
# print(zp_all[0])
