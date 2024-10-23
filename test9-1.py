string = input().split(" ")
even = [i for i in range(int(string[0]), int(string[1])) if i % 2 == 0]
odds = [i for i in range(int(string[0]), int(string[1])) if i % 2 != 0]
int9 = [i for i in range(int(string[0]), int(string[1])) if i % 9 == 0]
print("Кол-во четных: ", len(even), " ср. арифм.: ", sum(even) / len(even))
print("Кол-во нечетных: ", len(odds), " ср. арифм.: ", sum(odds) / len(odds))
print("Кол-во 9: ", len(int9), " ср. арифм.: ", sum(int9) / len(int9))




# even = 0
# even_numbers = []
# odds = 0
# odds_numbers = []
# int9 = 0
# int9_numbers = []
# for i in range(int(string[0]), int(string[1])):
#     if i % 2 ==0:
#         even += 1
#         even_numbers.append(i)
#     if i % 2 !=0:
#         odds += 1
#         odds_numbers.append(i)
#     if i % 9 == 0:
#         int9 += 1
#         int9_numbers.append(i)
# print("Кол-во четных: ", even, " ср. арифм.: ", sum(even_numbers) / even)
# print("Кол-во нечетных: ", odds, " ср. арифм.: ", sum(odds_numbers) / odds)
# print("Кол-во кр 9: ", int9, " ср. арифм.: ", sum(int9_numbers) / int9)


