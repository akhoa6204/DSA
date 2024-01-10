import math
def is_prime(n): 
    if n < 2: return False
    elif n == 2: return True 
    elif n % 2 == 0: return False
    canbac2_cuaN = int(math.sqrt(n)) + 1
    for i in range(3, canbac2_cuaN, 2):
        if n % i == 0: return False 
    return True 

number = int(input("Number: "))
result = is_prime(number)
print("result: ", result)
# 2C 