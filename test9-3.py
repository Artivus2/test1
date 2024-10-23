while True:
    chislo = int(input())
    if chislo == 7:
        print("Goodbye")
        break
    elif chislo > 0:
        print("Положительное")
    elif chislo < 0:
        print("Отрицательное")
    elif chislo == 0:
        print("Ноль")

