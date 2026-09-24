 
# tasks = []
# while True:
#    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
#    choice = input("Select an option: ")
#    if choice == '1':
#        task = input("Enter task: ")
#        tasks.append(task)
#        print("Task added successfully.")
#    elif choice == '2':
#        if tasks:
#            for i, t in enumerate(tasks, 1):
#                print(f"{i}. {t}")
#        else:
#            print("No tasks available.")
#    elif choice == '3':
#        if tasks:
#            for i, t in enumerate(tasks, 1):
#                print(f"{i}. {t}")
#            idx = int(input("Enter task number to delete: ")) - 1
#            if 0 <= idx < len(tasks):
#                print(f"Deleted: {tasks.pop(idx)}")
#            else:
#                print("Invalid index.")
#        else:
#            print("No tasks to delete.")
#    elif choice == '4':
#        print("Goodbye!")
#        break
#    else:
#        print("Invalid choice.")





print("ENTER A TASK")

print()
print("ENTER 1 TO ADD TASK  ")
print("ENTER 2 TO VIEW TASK  ")
print("ENTER 3 TO DELETE TASK  ")
print("ENTER 4 TO EXIT  ")

print()

a=int(input("ENTER  A VALUE : "))

if  a==1 :
    aa=input("ENTER A TASK : ")
    task=[]
    task.append(aa)
    print("TASK ADDED! ")
    # print(task)

elif a==2:
        pr