items=[]
prices=[]
sum=0
useri="" 
userp=0
while useri!="q":
    useri=input("product name(q for exit):").upper()
    userp=int(input("product price: "))

    if useri=="Q":
        break
    else:
        items.append(useri)
        prices.append(userp)
print("---------------Product name ---------------")
for i in items:
    print(i) 
for p in prices:
    sum+=p
    print("---------------------Total--------------")
    print(sum)  
if sum>=2000 :
        print("you get flat  10%  discout  on product ")
        a=2000/100*10 
        print(f"Your discounted price is :{a}")    
        b=sum-a
        print(f"your total value is :{b}")    



        