import math

def FunctionZ (a, b, c, x):
    z = (a + b**c + x**(a-b))/(c + math.sqrt(a + b))
    return z

constants = []    
f = open("constants_1_1.txt")
constants = (f.read().split())
f.close()
print("Please, enter x value: ")
x = float(input())
z = FunctionZ(float(constants[0]),float(constants[1]),float(constants[2]),x)
print("Function result: ", z)
f = open("result.txt", "w")
f.write("Function result: ", z)
f.close
