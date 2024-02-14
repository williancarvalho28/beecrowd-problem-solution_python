# beecrowd - 1010
# Simple Calculate

""" In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.
    Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.
    Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point. """

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