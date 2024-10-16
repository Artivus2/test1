string = input().split(" ")
begin = int(string[0])
end = int(string[1])

result = ""
for i in range(begin, end):
    if i % 7 == 0 and i != 0:
        result += str(i) + ","
        #print(i)
print(result)



