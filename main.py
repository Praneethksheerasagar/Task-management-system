from user import create_user, add_task, view_tasks, update_task, delete_task

def main():
    while True:
        print("\nTask Management System")
        print("1. Create a new user")
        print("2. Add a new task")
        print("3. View all tasks")
        print("4. Update a task")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            create_user(username)
            print(f"User '{username}' created.")

        elif choice == '2':
            username = input("Enter username: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            task = add_task(username, description, deadline)
            if task:
                print(f"Task added: {task}")
            else:
                print("User not found.")

        elif choice == '3':
            username = input("Enter username: ")
            tasks = view_tasks(username)
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found or user not found.")

        elif choice == '4':
            username = input("Enter username: ")
            task_id = int(input("Enter task ID: "))
            description = input("Enter new description (leave blank to keep current): ")
            deadline = input("Enter new deadline (leave blank to keep current): ")
            task = update_task(username, task_id, description, deadline)
            if task:
                print(f"Task updated: {task}")
            else:
                print("Task not found or user not found.")

        elif choice == '5':
            username = input("Enter username: ")
            task_id = int(input("Enter task ID: "))
            delete_task(username, task_id)
            print("Task deleted.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
