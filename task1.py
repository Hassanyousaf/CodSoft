import json
from datetime import datetime, timedelta

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None):
        self.tasks.append({"task": task, "due_date": due_date, "completed": False, "timestamp": str(datetime.now())})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            due_date = task["due_date"] if task["due_date"] else "No due date"
            print(f"{index}. {task['task']} (Due: {due_date}, Status: {status}, Added on: {task['timestamp']})")

    def update_task(self, task_index, new_description):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["task"] = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task index.")

    def set_due_date(self, task_index, due_date):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["due_date"] = due_date
            print("Due date set successfully!")
        else:
            print("Invalid task index.")

    def save_to_file(self, filename="todo_list.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename="todo_list.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

# Create a todo list
my_todo_list = TodoList()
my_todo_list.load_from_file()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Complete")
    print("5. Set Due Date")
    print("6. Save and Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        task_description = input("Enter task description: ")
        due_date_input = input("Enter due date (YYYY-MM-DD, optional): ")
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d") if due_date_input else None
        my_todo_list.add_task(task_description, due_date)
        print("Task added successfully!")

    elif choice == "2":
        my_todo_list.view_tasks()

    elif choice == "3":
        task_index = int(input("Enter the task index to update: "))
        new_description = input("Enter the new task description: ")
        my_todo_list.update_task(task_index, new_description)

    elif choice == "4":
        task_index = int(input("Enter the task index to mark as complete: "))
        my_todo_list.complete_task(task_index)

    elif choice == "5":
        task_index = int(input("Enter the task index to set the due date: "))
        due_date_input = input("Enter due date (YYYY-MM-DD): ")
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
        my_todo_list.set_due_date(task_index, due_date)

    elif choice == "6":
        my_todo_list.save_to_file()
        print("To-do list saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
