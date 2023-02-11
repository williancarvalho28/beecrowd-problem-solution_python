#beecrowd - 1098
# Sequence IJ 4   
I = 0
J = 1
while (I <= 2):
    for i in range (0, 3):
        if (I == 0.0) or (I == 1) or (I > 1.8):
            print(f'I={I:.0f} J={J:.0f}')
        elif (I < 2):
            print(f'I={I:.1f} J={J:.1f}')
        J+=1
    I = I + 0.2
    J = I + 1