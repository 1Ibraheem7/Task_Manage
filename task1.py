def task():
    tasks = []
    print("----- Welcome To Task Management App -----")

    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    while True:
        print("\nToday's tasks are:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

        print("\nEnter:")
        print("1 - Add a new task")
        print("2 - Update an existing task")
        print("3 - Delete a task")
        print("4 - View all tasks")
        print("5 - Exit/Stop")

        operation = int(input("Choose an operation: "))
        
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted...")
            else:
                print(f"Task '{del_val}' not found.")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid operation. Please enter a number between 1 and 5.")

task()
