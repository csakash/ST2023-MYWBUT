"""
Objective: To plan our day

We want to create a todo application
that will plan our day

Features of the app

- User can register
- User can add a task
    - update a task
    - delete a task
- User can see all the tasks
- User can mark the tasks as completed

{
    "username": 
}

"""

import json

with open("todoDB.json", "r") as f:
    todoData = json.load(f)
    print(todoData, type(todoData), len(todoData))

task_count = 0

while True:
    if len(todoData) == 0:
        print("Welcome to TodoCLI")
        print("Please enter your details")
        data = {}

        name = input("Please enter your name: ")
        data["name"] = name
        username = input("Please enter your username: ")
        data["username"] = username
        print(data)
        print("Please start adding your tasks and planning your day")
        print("To add tasks please enter: 'add-task'  or 'create-task'")
        print("To view tasks please enter: 'view-task'")
        print("To update tasks please enter: 'update'")
        print("To delete tasks please enter: 'delete-task'")

        cmd = input(">>>")

        if cmd == "add-task" or cmd == "create-task":
            # Enter the task additio logic
            if "tasks" not in data.keys():
                data["tasks"] = []

            
            task_name = input("Please enter task name: ")
            task_time = input("Please enter task time: (in military time format) ")
            
            task_count = task_count + 1
            task_dict = {
                "task_id": task_count,
                "task_name": task_name,
                "time": task_time,
                "completed": False
            }

            data["tasks"].append(task_dict)
            
            todoData = data

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
    else:
        with open("todoDB.json", "r") as f:
            data = json.load(f)
        # print(data, type(todoData), len(todoData))

        updated_count = int(data["tasks"][-1]["task_id"])
        task_count = updated_count
        cmd = input(">>>")
        
        if cmd == "add-task" or cmd == "create-task":
            # Enter the task additio logic
            if "tasks" not in data.keys():
                data["tasks"] = []

            task_name = input("Please enter task name: ")
            task_time = input("Please enter task time: (in military time format) ")
            task_count = task_count + 1
            task_dict = {
                "task_id": task_count,
                "task_name": task_name,
                "time": task_time,
                "completed": False
            }

            data["tasks"].append(task_dict)
            
            todoData = data

            with open("todoDB.json", "r+") as f:
                json.dump(todoData, f, indent=4)

        elif cmd == "view-task":
            with open("todoDB.json", "r") as f:
                temp = json.load(f)

            print(temp["tasks"])
        elif cmd == "update":
            pass
            #enter the logic of update
        elif cmd == "delete-task":
            pass




