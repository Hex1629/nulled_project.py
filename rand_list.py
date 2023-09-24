import random

with open('got.Lst','a') as f:
    for _ in range(int(input('TOTAL NEED ?'))):
     f.write(f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}/0\n')
