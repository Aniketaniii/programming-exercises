class phone:
    def __init__(a,brand,model,year):
       a.brand=brand
       a.model=model
       a.year=year


    def info(a):
        print(f"This is {a.brand} {a.model} launch in  {a.year}")
    
    
myphone=phone("samsung","s26","2026")
myphone.info()        


class registration:
    def __init__(a,name,surname,qualification,emailid ,phone):
        a.n=name
        a.s=surname
        a.q=qualification
        a.e=emailid
        a.p=phone

    def information(a):
         print(f"name : {a.n} ")
         print(f"surname : {a.s}")
         print(f"qualifiaction : {a.q}")
         print(f"emailid : {a.e}")
         print(f"phone : {a.p}")
        
name=input("ENTER YOUR NAME : ")
surname=input("ENTER YOUR SURNAME : ")
qual=int(input("ENETR YOUR QUALIFICATION : "))
email=input("ENETR YOUR EMAIL : ")
phon=int(input("ENETR YOUR PHONE : "))

myinfo=registration(name,surname,qual,email,phon)
myinfo.information()



