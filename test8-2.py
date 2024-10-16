string = input().split(" ")
begin = int(string[0])
end = int(string[1])
# result = ""
# for i in range(begin, end + 1):
#     result += str(i) + " "
# print(result)
# result = ""
# j = end
# for i in range(begin, end + 1):
#     result += str(j) + " "
#     j -= 2
# print(result)
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
#         #print(i)
# print(result)
count = 0
for i in range(begin, end+1):
    if i % 5 == 0 and i != 0:
        count+=1
print(count)

