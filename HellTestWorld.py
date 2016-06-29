import math
import random

for i in range(1,80):
    a= ((math.sqrt(i+i)*i+i)*math.sqrt(random.randint(1, 100)))
    while a>100:
        a=a-100.1111111
    print(a)

print("End the program of HellTestWorld")
