#my idea behind is i want a store to do list items for a user like on the system (a permanent area) where if the user runs the application again, they can still see those same items.

#to do list item 1: complete/incomplete
#load existing items
#create a new item
#list items
#mark items as complete
#save items

import json
file_name = "todo_list.json"



def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}
    

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            return json.dump(tasks, file)
    except: 
        print("Failed  to save.")



def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task["description"]} | {status}")
        # print(task_list)
    

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else: 
        print("Description cannot be empty.")
    


def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")


def main():
    # save_tasks({"tasks": ["saved tasks in the file"]})
    tasks = load_tasks()
    

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")


        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye\n")
            break
        else:
            print("Invalid choice. Please try again.")



main()