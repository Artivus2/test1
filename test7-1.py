string = input()
#print(string)
if 0 < int(string) > 100:
    print("Введеные числа вне диапазона")
else:
    number = int(string)
    #print(number)
    if number % 3 == 0 and number % 5 != 0:   # 17 / 5 -> 3.2, 18 / 3 -> 5.0
        print("Fizz")
    if number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    if number % 15 == 0:
        print("Fizz Buzz")
    else:
        print("Число: ",number)


