def Fact(num):
    result = 1
    
    while num >0:
        result *= num
        num-=1
    
    return result

print(Fact(3))

print('---')
import math

def Fact2(num):
    result = math.factorial(num)
    return result

print(Fact2(3))
