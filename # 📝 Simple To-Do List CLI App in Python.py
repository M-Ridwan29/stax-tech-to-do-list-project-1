# 📝 Simple To-Do List CLI App in Python

import os
import json

FILE_NAME = "todo_data.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

# Display task list
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📋 Your To-Do List:\n")
        for idx, task in enumerate(tasks, 1):
            status = "✔️" if task["done"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
