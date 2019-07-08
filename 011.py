def Fact():
    result = 1
    num = 5
    
    while num >0:
        result *= num
        num-=1
    
    return result

print(Fact())

print('---')
import math

def Fact2():
    result = math.factorial(5)
    return result

print(Fact2())
