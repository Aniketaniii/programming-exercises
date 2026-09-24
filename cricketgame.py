 
import random as r
print("|---------- CRICKET GAME ----------|")

# Toss=input("HEAD OR TAIL : ")
# print(Toss)

# if Toss == head:
#     print("you choose head ")
#     choose=input(" what you want bat or bowl : ")
#     if choose==bat:
#         print("You won the toss and optained to bat first ")
#     else :
#         print("You won the toss and optained to bowl first  ")
# else:
#     print("you loose toss")        

score=0
computer =0
player1=0

# while player1!=computer:

for i in range(1,6) :
        

        player1=int(input("Enter a number between 1 to 6 : "))
        print(player1)

        computer=r.randint(1,6)
        print(computer)

        if player1==computer :
                print("out")
        elif player1>computer :
                print(f"you scored {player1}")
        elif player1<computer:
                print(f"you scored {player1}")

        score+=player1
        print(f"Player scored :{score} ")
        break