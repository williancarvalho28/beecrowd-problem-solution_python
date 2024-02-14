# beecrowd - 1007
# Difference

""" Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).
    Input
The input file contains 4 integer values.
    Output
Print DIFERENCA (DIFFERENCE in Portuguese) with all the capital letters, according to the following example, with a blank space before and after the equal signal. """

A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = ((A*B)-(C*D))
print(f'DIFERENCA = {DIFERENCA}')