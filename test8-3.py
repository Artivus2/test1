
string = input().split(" ")
begin = int(string[0])
end = int(string[1])
result = ""

for i in string:
    if i % 3 == 0 and i % 5 != 0:  # 17 / 5 -> 3.2, 18 / 3 -> 5.0
        result = result + "Fizz: " + str(i) + ", "
    if i % 5 == 0 and i % 3 != 0:
        result += "Buzz: " + str(i) + ", "
    if i % 15 == 0:
        result += "Fizz Buzz: " + str(i) + ", "
    else:
        result += "Число: " + str(i) + ", "

