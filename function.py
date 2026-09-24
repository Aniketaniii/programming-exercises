# def sum():
#     print(5+5)
   

# def add(a,b):
#     print(a+b)



# def iseven (num):
#     if num %2==0:
#         print(f"{num}is an odd number ")
#     else:
#         print(f"{num}is an odd number")    

# iseven(123984093)       


# def numberguessing (num):
#     while True :
#         user=int(input("Guess the number between 1-100 : "))
#         if user< num:
#             print("your number is smaller guess it again")
#         elif user>num:
#             print("your number is greater guess it again ")
#         else:
#             print("you won ")   
#             break         

# numberguessing(55)    

def evenloop():
    n=int(input("Enter an endpoint : "))

    for i in range(1,n):
        if i%2==0:
            print(i)
    
evenloop()