# beecrowd - 1021
# Banknotes and Coins

""" Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.
    Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).
    Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example. """

reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

notas = [100, 50, 20, 10, 5, 2]
print('NOTAS:')
for nota in notas:
    print(f'{centavos//(nota*100)} nota(s) de R$ {nota}.00')
    centavos = centavos%(nota*100)
    
moedas = [100, 50, 25, 10, 5, 1]
print('MOEDAS:')
for moeda in moedas:
    print(f'{centavos//moeda} moeda(s) de R$ {moeda//100}.{moeda%100:02}')
    centavos = centavos%moeda