a = 4
if a > 2:
    print("Matched")
    print("Second line")
else:
    print("Not Matched")
print("if else block code is completed")

obj = [1, 3, 5, 7, 11, 9]
for i in obj:
    print(i * 2)

#range(i,j) = i to j-1
summation = 0
for j in range(1, 6):
    print(j)
    summation = summation + j
print("{} {}".format("sum of the first 5 numbers is ", summation))

for k in range(1, 10, 2):
    print(k)  # 1 3 5 7 9
for a in range(5):
    print(a)  # 0 1 2 3 4
print("For loop block code is completed")

