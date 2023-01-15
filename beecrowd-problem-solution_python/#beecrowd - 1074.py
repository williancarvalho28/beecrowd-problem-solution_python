#beecrowd - 1074
# Even or Odd

n = int(input())
for i in range(0, n):
    x = int(input())
    if (x > 0 and x % 2 == 0):
        print("EVEN POSITIVE")
    elif (x > 0 and x % 2 != 0):
        print("ODD POSITIVE")
    elif (x == 0):
        print("NULL")
    elif (x < 0 and x % 2 != 0):
        print("ODD NEGATIVE")
    else:
        print("EVEN NEGATIVE")
        