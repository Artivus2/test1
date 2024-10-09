import re
string = input("введите число")

if float(string) > 0:
    print("положительное")
elif float(string) < 0:
    print("отрицательное")
else:
    print("число равно 0")








# number = [0, 0]
# print(re.findall(r'[-+^.]?\d+', string))
# numbers = re.findall(r'[-+^.]?\d+', string)
# try:
#     number[0] = float(numbers[0])
# except:
#     number[0] = 0
# try:
#     number[1] = float(numbers[1])
# except:
#     number[1] = 0
#

