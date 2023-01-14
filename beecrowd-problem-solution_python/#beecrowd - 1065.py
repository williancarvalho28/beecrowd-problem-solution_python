#beecrowd - 1065
# Even Between five Numbers

number = 0
cont = 0

for i in range(0, 5):
    number = int(input())
    if (number%2 == 0):
        cont += 1
print(f'{cont} valores pares')
