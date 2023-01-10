#beecrowd - 1017
# Fuel Spent 
hours = int(input())
speed = int(input())
amount_of_spent_fuel_liters  = 12
liters_needed = (hours*speed)/amount_of_spent_fuel_liters
print(f'{liters_needed:.3f}')

