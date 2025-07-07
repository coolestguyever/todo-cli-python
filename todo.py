

tasks = [] #list that will contain all the tasks


def load_tasks(): #loads all the tasks from a saved file
        try:
            with open('tasks.txt', 'r') as tasks_file:
                for task in tasks_file:
                    tasks.append(task.strip())
        except FileNotFoundError:
            pass

def save_tasks(): #saves all the tasks to a file
    with open('tasks.txt','w') as tasks_file:
        for task in tasks:
            tasks_file.write(task + '\n')


def add_task(): #will add tasks to the list
    task = input("Enter a task: ").strip()
    tasks.append(task)
    save_tasks()
    print("Task added!")

def view_tasks(): #will display all the tasks in the list
    if len(tasks) == 0:
        print("No tasks added.")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(): #will delete task from list
    if len(tasks) == 0:
        print("No tasks added.")
    else:
        view_tasks()
        x = int(input("Which task would you like to delete?"))
        if x<0 or x>len(tasks):
            print("Invalid input.")
        else:
            confirm = input(f"Delete task '{tasks[x - 1]}'? (y/n): ").lower()
            if confirm == 'y':
                tasks.pop(x - 1)
                print("Task deleted!")
            else:
                print("Cancelled.")

def main(): #main function
    load_tasks()
    while True:
        print("\n****** TO-DO Application ******")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        try:
            x = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        match x:
            case 1:
                view_tasks()
            case 2:
                add_task()
            case 3:
                delete_task()
            case 4:
                print("Have a great day!")
                break
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()






