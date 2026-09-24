class student :
    def __init__(s,name,age,marks):
        s.n=name
        s.a=age
        s.m=marks

    def display(s):   
        print("---------------STUDENT DETAILS--------------")
        print(f"NAME : {s.n}")
        print(f"AGE : {s.a}")
        print(f"marks : {s.m}")
        print("--------------------------------------------")

n=int(input("HOW MANY STUDENTS?:  "))
children=[]

for i in range(n):
    print(f"ENTER STUDENT {i+1} DETAILS ")
    name=input("NAME : ")
    age=int(input("AGE : "))
    marks=int(input("marks : "))

    s=student(name,age,marks)
    children.append(s)

for s in children : 
    s.display()   