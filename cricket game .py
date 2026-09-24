def firstplayer():

    
    import random as r

    
    for i in range(1,6):
        player1=int(input("Enter a number between 1 to 6 : "))
        print(player1)

        computer=r.randint(1,6)
        print(computer)

        total=0
        
        if player1==computer:
            print("out")
        elif player1>computer:
            print(f"you scored {player1}")
        else:
            print(f"you scored {player1}")

    total+=player1
    print(f"total scored is {total}")




import random as r

computer=0
while computer!=True :
    for i in range(1,6):
            player1=int(input("YOU ARE BOWLING NOW CHOOSE NUMBER BETWEEN 1 to 6 : "))
            print(player1)

            computer=r.randint(1,6)
            print(computer)

            total=0
            
            if player1==computer:
                print("out")
            elif player1>computer:
                print(f"you scored {computer}")
            else:
                print(f"you scored {computer}")

            total+=computer
            print(f"total scored is {total}")
    break
