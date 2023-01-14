#beecrowd - 1071
# Sum of Consecutibe Odd Numbers 1

x = int(input())
y = int(input())
sum = 0

for i in range((y+1), x):
    if (i % 2 != 0):
        sum += i
print(sum)
