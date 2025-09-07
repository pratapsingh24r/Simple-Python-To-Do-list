
#Data of To-Do list.

tasks = []

with open("to_do_list.txt", "r") as f:
   for line in f:
       cleanl = line.strip()
       task, status = cleanl.split(" - ")

       dic =  {"task": task, "status": status}   
       tasks.append(dic)

while True:
    try:
        print("\n\tMenu:")
        print("1.Add task")
        print("2.View task")
        print("3.Mark done as completed")
        print("4.Delete task")
        print("5.Save/Exit")

        user = int(input("Choose from (1-5): "))
#add task
        if user == 1:
            add = input("Enter your task to add: ")
            tasks.append({"task": add, "status": "pending"})
            print("\nYour task added successfully.")
#view task
        elif user == 2:
            if not tasks:
                print("\nNo tasks available.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t['task']} [{t['status']}]")

#mark done           
        elif user == 3:
            done = int(input("Enter number of completed tasks: "))
            if 1<= done <= len(tasks):
                tasks[done - 1]["status"] = "done"
                print("\nTask marked as completed.")
                
            else:
                print("\nInvalid task number.")

#remove
        elif user== 4:
            remove = int(input("Enter task number to delete: "))
            if 1<= remove <= len(tasks):
                tasks.pop(remove - 1 )
                print("\nTask removed.")
            else: 
                print("\nInvalid task number.")
#exit                
        elif user == 5:
           with open("to_do_list.txt", "w") as f:
            for t in tasks:
                f.write(f"{t['task']} - {t['status']}")
                print("\nTasks saved to file. Exiting  program.")
                
        else:
            print("\nWrong Input! try again.")
           


    except ValueError:
        print("\nInvalid input, Please try again.")

    
     
