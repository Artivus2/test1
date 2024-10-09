
string = input().split(" ")
"""
сортировка пузырьковая
"""
numbers =[]
for i in string:
    numbers.append(int(i))
numbers.sort(reverse=True)

print(numbers)









# if int(string[0]) == int(string[1]):
#     print("Числа равные", string[0])
# else:
#     if int(string[0]) > int(string[1]):
#         print("2 число: ", int(string[1]))
#         print("1 число: ", int(string[0]))
#     else:
#         print("1 число: ", int(string[0]))
#         print("2 число: ", int(string[1]))