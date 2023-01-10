#beecrowd - 1018
# Banknotes
n  = int(input())
print(n)
nota100 = n//100
n = n%100
nota50 = n//50
n = n%50
nota20 = n//20
n = n%20
nota10 = n//10
n = n%10
nota5 = n//5
n = n%5
nota2 = n//2
n = n%2
nota1 = n//1
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')


