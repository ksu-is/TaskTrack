tasks = []


def addTask():
    task= input("Please enter a task: ")
    priority = input("Please enter a priority (1 for high, 2 for medium, 3 for low): ")
    tasks.append((task, priority))
    print(f"Task '{task}' with priority {priority} added to the list.")


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else: 
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid input.")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")  
    else:
        print("Current tasks:")    
        for index, (task, priority) in enumerate(tasks):
            print(f"Task #{index}. {task} (Priority: {priority})")


def prioritizeTask():
    listTasks()
    try:
        taskToPrioritize = int(input("Enter the number of the task to prioritize: "))
        if taskToPrioritize >=0 and taskToPrioritize < len(tasks):
            new_priority = input("Enter new priority (1 for high, 2 for medium, 3 for low): ")
            task, _ = tasks[taskToPrioritize]
            tasks[taskToPrioritize] = (task, new_priority)
            print(f"Task #{taskToPrioritize} priority updated to {new_priority}.")
        else:
            print(f"Task #{taskToPrioritize} was not found")    
    except: 
        print("Inavlid input.")


def sortTasks():
    listTasks()
    try:
        sort_choice = input("Sort by (1. Priority, 2. Category): ")
        if sort_choice == "1":
            tasks.sort(key=lambda x: x["priority"])
            print("Tasks sorted by priority:")
            listTasks()
        elif sort_choice == "2":
            tasks.sort(key=lambda x: x["category"])
            print("Tasks sorted by category:")
            listTasks()
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")



        
if __name__ == "__main__":
    ### Create a loop to run the app
    print("Welcome to the TaskTrack App! :) You will be able to add, delete, list, and prioritize tasks, as well as exit the app when needed. After exiting, the choices will no longer appear, and the current data will not be saved, so please keep that in mind. The overall goal is to help users with their productivity.")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Prioritize task(s)")
        print("5. Quit")

        choice = input("Enter your choice: ")
        
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):
            prioritizeTask()
        elif(choice=="5"):
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye! :)")
