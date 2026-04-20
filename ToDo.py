
#menu app
def show_menu ():
    print("\n ===MENU===")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4. Quit")
        
# view task function
def view_tasks(tasks):
    if not tasks: 
        print("No tasks to view.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
# add task function
def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")
    
# delete task function
def delete_task(tasks):
    if not tasks:
        print ("No tasks to delete")
        return
    view_tasks(tasks) 
#error handling
    try:
        num = int(input("Enter the number of the task you would like to delete:"))
    except ValueError:
         print("Not a valid number")
    else:
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print (f"Removed: {removed}")
        else:
            print("Task does not exist")
    finally:
        print("Returning to menu...")
        

#greeting function
def main ():
    print("Welcome to your To-Do List!")
    
    tasks = [] 
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print ("Goodbye!")
            break
        else:
            print("Invalid menu option")
        

if __name__ == "__main__":
    main()
        


        
        
    
    