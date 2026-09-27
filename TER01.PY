import os
FILE_NAME = "tasks.txt"
print("""Hello Sir, Welcome to the TER01 program. This program is designed to help you with your tasks .
      1. Task 1: Add task
      2. Task 2: View tasks
      3. Task 3: Delete task
      4. Task 4: exit""")
while True:
    task_number = int(input("Please enter the task number you want to perform: "))
    if task_number == 1:
        print("write your task here please :")
        task = input()
        with open(FILE_NAME, "a", encoding="utf-8") as file:
         file.write(task + "\n")
        print("Task saved successfully!")
        continue
    elif task_number == 2:
        print("Viewing tasks...")
        print("Tasks:")
        if os.path.exists(FILE_NAME):
         print("\n--- Your Tasks ---")
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = file.readlines() 
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found yet!")
        continue
    elif task_number == 3:
        print("Deleting task...")
        if os.path.exists(FILE_NAME):
         with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        print("Task deleted successfully!")
        continue
    elif task_number == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid task number. Please try again.")
