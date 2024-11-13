import datetime
import json
import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file if it exists"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description, due_date=None):
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'Pending',
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("\nTask added successfully!")

    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\nYour To-Do List:")
        print("-" * 80)
        for task in self.tasks:
            print(f"\nTask ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created: {task['created_at']}")
            if task['due_date']:
                print(f"Due Date: {task['due_date']}")
            print("-" * 80)

    def update_task(self, task_id, status):
        """Update task status"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                self.save_tasks()
                print(f"\nTask {task_id} updated successfully!")
                return
        print(f"\nTask {task_id} not found!")

    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"\nTask {task_id} deleted successfully!")
                return
        print(f"\nTask {task_id} not found!")

def main():
    todo = TodoList()
    
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            if due_date.strip() == "":
                due_date = None
            todo.add_task(title, description, due_date)
            
        elif choice == '2':
            todo.view_tasks()
            
        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            print("\nAvailable statuses:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")
            status_choice = input("Enter status choice (1-3): ")
            status_map = {'1': 'Pending', '2': 'In Progress', '3': 'Completed'}
            if status_choice in status_map:
                todo.update_task(task_id, status_map[status_choice])
            else:
                print("Invalid status choice!")
            
        elif choice == '4':
            task_id = int(input("Enter task ID: "))
            todo.delete_task(task_id)
            
        elif choice == '5':
            print("\nThank you for using the To-Do List Application!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()