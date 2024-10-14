string = input("введите число и степень: ").split(" ")
number = int(string[0])
stepen = int(string[1])

if 0 <= stepen <= 7: #stepen > 0 and stepen <= 7
    result = number ** stepen
    print("Результат: ", result)

