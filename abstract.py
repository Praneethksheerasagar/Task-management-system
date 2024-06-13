class Task:
    def __init__(self, id, description, deadline):
        self.id = id
        self.description = description
        self.deadline = deadline

    def __str__(self):
        return f"Task(ID: {self.id}, Description: {self.description}, Deadline: {self.deadline})"


class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, description=None, deadline=None):
        for task in self.tasks:
            if task.id == task_id:
                if description:
                    task.description = description
                if deadline:
                    task.deadline = deadline
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]


class TaskManager:
    def __init__(self):
        self.users = {}
        self.task_history = []

    def add_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        return self.users.get(username, None)

    def push_history(self, operation):
        self.task_history.append(operation)

    def pop_history(self):
        return self.task_history.pop() if self.task_history else None
