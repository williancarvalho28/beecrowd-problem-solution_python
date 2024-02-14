# beecrowd - 1013
# The greatest

""" Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:
    Input
The input file contains 3 integer values.
    Output
Print the greatest of these three values followed by a space and the message “eh o maior”. """

[A, B, C] = map(int, input().split())
maior = max(A, B, C)
print(f'{maior} eh o maior')