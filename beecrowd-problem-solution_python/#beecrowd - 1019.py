#beecrowd - 1019
# Time Conversion
second = int(input())
hour = second//3600
second = second%3600
minutes = second//60
second = second%60

print(f'{hour}:{minutes}:{second}')