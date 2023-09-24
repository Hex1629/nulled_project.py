import random

with open('got.Lst','a') as f:
    for _ in range(250):
     f.write(f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}/0\n')
