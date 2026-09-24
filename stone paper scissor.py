import random 

print("|-------------------ROCK ,PAPER AND SCISSOR-------------------|\n")
choicess= ("stone","paper","scissor")
user=None


running=True
while running :
    computer=random.choice(choicess)
    user=input("Enter your choice('stone','paper','sissor'): ").lower()
    while user not in choicess:
        user=input("Enter your choice ('stone','paper','scissor'): ").lower()

    print(f"YOU ENTER VALUE IS  : {user}")
    print("COMUTER VALUE IS    : ",computer)

    if user==computer:
            print("It's  Tie")
    elif user=="stone" and computer=="scissor":
            print("You won")
    elif user=="scissor" and computer=="paper":
            print("You won")
    elif user=="paper" and computer=="stone":
            print("You won")
    else:
            print("you losse it ")
    if input("WANT TO PLAY IT AGAIN (ENTER 'Y' EITHER 'N' FOR NOT PLAYING :)")!="y":
             running =False

print("|-------------------Thanks for playing -------------------|")