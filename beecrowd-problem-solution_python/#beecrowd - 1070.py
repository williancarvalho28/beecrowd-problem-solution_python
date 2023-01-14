#beecrowd - 1070
# Six Odd Numbers

number = int(input())
i = 0
while(i < 6):
    if(number % 2 != 0):
        print(number)
        i = i + 1
    number = number + 1