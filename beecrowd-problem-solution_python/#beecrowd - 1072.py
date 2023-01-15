#beecrowd - 1072
# Interval 2

n = int(input())
x_out = 0
x_in = 0
for i in range(0, n):
    x = int(input())
    if (x <= 20 and x >= 10):
        x_in += 1
    else:
        x_out += 1

print(f'{x_in} in')
print(f'{x_out} out')