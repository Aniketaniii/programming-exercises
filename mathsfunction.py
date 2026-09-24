import math
a=int(input("Enter an Integer: "))
b=int(input("Enter an Integer: "))

add=a+b
print(f" {a} + {b} ={add}")

a+=b
a*=34
sub=a-b

print(f"{a} - {b}={sub}")

num=int(input("Enter a value for sqrt : "))
# result=math.sqrt(num)
result=math.pow(num,2)
print(result)   
