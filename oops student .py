class student:
    def __init__(s,name,age,marks):
        s.name=name
        s.age=age
        s.marks=marks

    def display(s):
        print("---------------STUDENT DETAILS---------------")

        print(f"NAME : {s.name}")
        print(f"AGE  : {s.age}")
        print(f"marks: {s.marks}")
    
        print("---------------------------------------------")

n=int(input("ENTER HOW MANY STUDENTS DETAILS REQUIRED :  "))


for i in range(n):

    a=input("ENTER YOUR NAME : ")
    b=int(input("ENTER YOUR AGE : "))
    c=int(input("ENTER YOUR MARKS :  "))
    print()
    print()


    mydetail=student(a ,b ,c)
    mydetail.display()
        