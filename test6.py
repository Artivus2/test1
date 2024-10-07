#
# string = input("введите тир числа").split(" ")
# numbers = []
# for i in string:
#     numbers.append(float(i))
#
# print("Max:" + str(max(numbers)))
# print("Min: ", min(numbers))
# print("Avg " + str(sum(numbers) / len(numbers)))
# print(f"Avg {str(sum(numbers) / len(numbers))} ")


string = input().split(" ")
number1 = float(string[0])
znak = string[1]
if znak == "m":
    result = (number1 * 0.000621).__format__(".5f")
    print("Mile",result)
elif znak =="d":
    result = (number1 * 39.3701).__format__(".5f")
    print("Dyim",result)
elif znak =="y":
    result = (number1 * 1.09361).__format__(".5f")
    print("Yards",result)
else:
    print("неккорректные данные")








