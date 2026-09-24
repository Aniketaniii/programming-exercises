menu={"popcorn":200,"pizza":300,"fries":200,"burger":100}

cart=[]
total=0

for keys,values in menu.items():
    print(f"{keys} : {values}")

while True:
    food=input("Enter your product(q for quit ): ")

    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for f in cart:
    print(f)