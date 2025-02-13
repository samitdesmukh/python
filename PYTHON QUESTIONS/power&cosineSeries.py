def power(base,exp):
    if exp ==0:
        return 1
    else:
        return base*power(base, exp-1)
base = int(input("Enter base:"))
exp = int(input("Enter exponential value:"))

result= power(base,exp)
print("Result:",result)

#cos series
import math
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
def cos_series(x,terms):
    x=math.radians(x)
    cos_x=0
    for i in range(terms):
        term= ((-1)**i)*(x**(2*i))/factorial(2*i)
        cos_x += term
    return cos_x
x= float(input("Enter the value of x in degrees:"))
terms = int(input("Enter the number of the terms"))
result= cos_series(x,terms)
print(result)
