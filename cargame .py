import random

# Base Class
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def move(self):
        move_distance = random.randint(1, self.speed)
        self.distance += move_distance
        print(f"{self.name} moves {move_distance} units (Total: {self.distance})")


# Subclass: Car
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, speed=10)

    def move(self):
        print(f"{self.name} accelerates 🚗")
        super().move()


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, speed=8)

    def move(self):
        print(f"{self.name} zooms 🏍️")
        super().move()


# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name, speed=6)

    def move(self):
        print(f"{self.name} rumbles 🚚")
        super().move()


# Game Logic
def race(player, opponent):
    finish_line = 50
    print("\n🏁 Race Start!\n")

    while player.distance < finish_line and opponent.distance < finish_line:
        input("Press Enter to move...")

        player.move()
        opponent.move()

        print("-" * 40)

    # Winner
    if player.distance >= finish_line and opponent.distance >= finish_line:
        print("\n🤝 It's a tie!")
    elif player.distance >= finish_line:
        print(f"\n🏆 {player.name} wins the race!")
    else:
        print(f"\n🏆 {opponent.name} wins the race!")


# Main Program
print("Choose your vehicle:")
print("1. Car")
print("2. Bike")
print("3. Truck")

choice = input("Enter choice (1/2/3): ")
name = input("Enter your vehicle name: ")

if choice == "1":
    player = Car(name)
elif choice == "2":
    player = Bike(name)
else:
    player = Truck(name)

# Opponent (random)
opponent = random.choice([Car("Enemy Car"), Bike("Enemy Bike"), Truck("Enemy Truck")])

# Start race
race(player, opponent)






# import random as r

# class vehical():
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed


# class car():
#     def carcall():
#         a=input("ENTER YOUR VEHICAL NAME : ")       
#         print(f"") 