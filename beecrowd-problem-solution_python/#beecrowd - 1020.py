#beecrowd - 1020
# Age in days
age_in_days = int(input())
ano = age_in_days//365
age_in_days = age_in_days%365
mes = age_in_days//30
age_in_days = age_in_days%30
dia = age_in_days

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')