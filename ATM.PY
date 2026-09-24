print("|----------WELCOME TO ATM----------|\n")

print("Enter 1 to check balance  ")
print("Enter 2 to deposite cash  ")
print("Enter 3 to withraw cash   ")
print("Enter 4 to exit          \n ")

a=int(input("Enter a number : \n"))

x=100000
while a!=4 :

 if a == 1 :
    print("Your balance is : \n",x)
    a=int(input("Enter a number : "))

 elif a==2 :
    deposite=int(input("Enter amount to deposite cash : "))
    b=x+deposite
    print("Your total balance  is : \n",b)
    a=int(input("Enter a number : "))
 elif a==3:
    withdraw=int(input("Enter amount to withdraw cash : "))
    c=x-withdraw
    print("Your total balance is : \n",c)
    a=int(input("Enter a number : "))

 elif a==4: 
    print("Thank you ")



