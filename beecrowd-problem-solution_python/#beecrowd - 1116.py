#beecrowd - 1116
# Dividing X by Y

n = int(input())
for i in range (0, n):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if (y != 0):
        div = x/y
        print(f'{div:.1f}')
    else:
        print('divisao impossivel')
        