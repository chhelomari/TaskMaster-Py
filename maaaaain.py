import json
import os

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=2)

    def add_task(self, task):
        self.todos.append({"task": task, "done": False})
        self.save_todos()
        print(f"Added task: {task}")

    def list_tasks(self):
        if not self.todos:
            print("No tasks yet!")
        for i, t in enumerate(self.todos, 1):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. [{status}] {t['task']}")

    def mark_done(self, task_number):
        if 1 <= task_number <= len(self.todos):
            self.todos[task_number - 1]["done"] = True
            self.save_todos()
            print(f"Marked task {task_number} as done!")
        else:
            print("Invalid task number.")

def main():
    app = TodoApp()
    while True:
        print("\nOptions: list, add, done, quit")
        choice = input("Choose an option: ").lower()
        if choice == "list":
            app.list_tasks()
        elif choice == "add":
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == "done":
            num = int(input("Task number to mark done: "))
            app.mark_done(num)
        elif choice == "quit":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
