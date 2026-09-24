print("|---------- MARKSHEET  PROGRAM ----------|\n")

print("|----- Enter your all  marks as per required -----|\n")
a=int(input("Enter your  English   marks: "))
b=int(input("Enter your  Maths     marks: "))
c=int(input("Enter your  Physcics  marks: "))
d=int(input("Enter your  Chemistry marks: "))
e=int(input("Enter your  Biology   marks: "))
f=int(input("Enter your  Hindi     marks: "))

x=a+b+c+d+e+f
print(f"Your total marks is {x} ")

percentage= x/600*100
print(f"Your percentage is {percentage}%")

if percentage >= 90:
    print("you scored a grade")
elif percentage >= 80:        
    print("you scored b grade")
elif percentage >=70:
    print("you scored c grade")
elif percentage >=60: 
    print("you scored d grade") 
elif percentage >=50:
    print("you scored e grade") 
elif percentage >=36:
    print("you scored f grade") 
elif percentage <=35:
    print("you are failed") 

print("|----------THANK YOU ----------|\n")               