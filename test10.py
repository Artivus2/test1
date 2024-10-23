a1 = 10
b1 = 20
matrix=[[1,2,3],[4,5,6],[7,8,9],["OK",[13,14,[15,16,"OK"]],12, b1]]
search = "OK"
for i in matrix:
    print("уровень 1", i)
    if search in i:
        print("нашли ОК1")
        break
    else:
        for vtoroy in i:
            print("2 уровень",vtoroy)
            if search == vtoroy:
                print("нашли ОК2")
                break
            else:
                if type(vtoroy) is list:
                    print(type(vtoroy))
                    for tretiy in vtoroy:
                        print(tretiy)
                        if search == tretiy:
                            print("нашли ОК3")
                            break
                        else:
                            if type(tretiy) is list:
                                for chetv in tretiy:
                                    print(chetv)
                                    if search == chetv:
                                        print("нашли ОК4")
                                        break




