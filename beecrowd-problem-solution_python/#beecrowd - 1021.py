#beecrowd - 1021
# Banknotes and Coins
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