#beecrowd - 1066
# Even, Odd, Positive and Negative

number = 0
cont_even, cont_odd, cont_pos, cont_neg = 0, 0, 0, 0

for i in range(0, 5):
    number = int(input())
    if (number%2 == 0):
        cont_even += 1
    else:
        cont_odd += 1
    if  (number > 0):
        cont_pos += 1
    elif (number < 0):
        cont_neg += 1
        
print(f'{cont_even} valor(es) par(es)')
print(f'{cont_odd} valor(es) impar(es)')
print(f'{cont_pos} valor(es) positivo(s)')
print(f'{cont_neg} valor(es) negativo(s)')