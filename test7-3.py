
string = input("Введите стоимость, с кого звоним, куда звоним").split(" ")
price = float(string[0])
# mtot = 0 # c мтс на теле 0.2 m
# mtob = 1 # c мтс на билайн 0.3 b
# ttob = 2 # с теле на билайн 0.4 t
# mtom = 3 # мтс  0.1
# btob = 4 # билайн 0.1
# ttot = 5 # теле 0.1
if string[1] =="m" and string[2]=="t":
    result = price * 0.2
    print(result)
    """
    TO DO
    """