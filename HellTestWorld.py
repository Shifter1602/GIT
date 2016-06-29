'''import math
import random

for i in range(1,80):
    a= ((math.sqrt(i+i)*i+i)*math.sqrt(random.randint(1, 100)))
    while a>100:
        a=a-100.1111111
    print(a)

print("End the program of HellTestWorld")'''

a=2
b=1
for i in range(1, 1999):
    l = "oooooooooooooooooooooooooooooo"
    for j in range(a):
        l=" "+l
    if a==152:
        b=-1
    elif a==2:
        b=1
    a+=b
    print(l)
    
