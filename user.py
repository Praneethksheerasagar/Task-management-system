from abstract import User, Task, TaskManager

task_manager = TaskManager()

def create_user(username):
    user = User(username)
    task_manager.add_user(user)
    return user

def add_task(username, description, deadline):
    user = task_manager.get_user(username)
    if user:
        task_id = len(user.tasks) + 1
        task = Task(task_id, description, deadline)
        user.add_task(task)
        task_manager.push_history(('add', task))
        return task
    return None

def view_tasks(username):
    user = task_manager.get_user(username)
    if user:
        return user.view_tasks()
    return []

def update_task(username, task_id, description=None, deadline=None):
    user = task_manager.get_user(username)
    if user:
        task = user.update_task(task_id, description, deadline)
        task_manager.push_history(('update', task))
        return task
    return None

def delete_task(username, task_id):
    user = task_manager.get_user(username)
    if user:
        task_manager.push_history(('delete', user.get_task_by_id(task_id)))
        user.delete_task(task_id)
