#
# a1 = 1
# a2 = 2
# a3 = 4
# a4 = 6
# a = [1, 2, 6, 10]
# b =[]
# print(b)
# for i in range(len(a)):
#     b.append(i+10)
# print(b)
# b.pop()
# print(b)
# b[2] = 300
# print(b)
# b.insert(1, 340)
# print(b)
# b.pop(2)
# print(b)
# print(list1 := [i*2 for i in range(100) if i % 3==0])
#
#
# list2 = []
# for i in range(100):
#     if i % 3 == 0:
#         i *= 2
#         list2.append(i)
# print(list2)

customers=[1,7,3,2,10]

#list2 = [i for i in customers]

print(sum(customers)) # to do
result = 1
for i in customers:
    print(i)
    result *= i
print(result)


