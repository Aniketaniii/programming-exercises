class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary

    def set_salary(self,salary):
        self.__salary=salary

    def get_salary(self):
        print(self.__salary)

e1=employee("aniket",20,30000)
e1.set_salary(100000)
e1.get_salary()
