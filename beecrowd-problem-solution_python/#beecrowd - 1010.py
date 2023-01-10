#beecrowd - 1010
# Simple Calculate
code, units, price = 0, 0, 0
valor_total = 0
for i in range(0,2):
    code, units, price = map(float, input().split(' '))
    code = int(code)
    units = int(units)
    valor_a_pagar = (price*units)
    valor_total += valor_a_pagar
    i += 1
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')