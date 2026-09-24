a=int(input("Enter a number: "))
b=input("Enter (+,-,/,*): ")
c=int(input("Enter a number: "))

add=a+c
sub=a-c
multiply=a*c
divide=a/c

if b=="+" :
    print(f"{add}")
elif b=="-":
    print(f"{sub}")
elif b=="/":
    print(f"{divide}")
elif b=="*":
    print(f"{multiply}") 
else :
    print("Enter only(+,-,*,/)") 
                       

