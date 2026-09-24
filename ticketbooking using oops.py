class booking :
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def info(self):
        print(f"NAME : {self.name} ")
        print(f"GENDER : {self.gender}")
        print(f"AGE : {self.age}")

n=int(input("HOW MANY TICKETS ?: "))
passenger=[]

for i in range(n):
   name=input("ENTER YOUR NAME : ")
   gender=input("ENTER YOUR GENDER : ")
   age=int(input("ENTER YOUR AGE : "))

   p=booking(name,gender,age)   
   passenger.append(p)

for p in passenger:
    p.info()