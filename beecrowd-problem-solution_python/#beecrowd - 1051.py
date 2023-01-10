#beecrowd - 1051
# Taxes
salary = float(input())

if (salary >= 0.00 and salary <= 2000.00):
    print("Isento")
elif (salary >= 2000.00 and salary <= 3000.00):
    calculo = salary - 2000.00
    total = calculo*0.08
    print(f'R$ {total:.2f}')
elif (salary >= 3000.00 and salary <= 4500.00):
    calculo = salary - 3000.00
    total = (calculo * 0.18) + (1000 * 0.08)
    print(f'R$ {total:.2f}')
else:
    calculo = salary - 4500.00
    total = (calculo * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {total:.2f}')