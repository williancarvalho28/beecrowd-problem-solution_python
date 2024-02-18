# beecrowd - 1020
# Age in days

""" Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”. Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.
    Input
The input file contains 1 integer value.
    Output
Print the output, like the following example. """

age_in_days = int(input())
ano = age_in_days//365
age_in_days = age_in_days%365
mes = age_in_days//30
age_in_days = age_in_days%30
dia = age_in_days

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')