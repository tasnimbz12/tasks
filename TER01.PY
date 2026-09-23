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
        print("Task saved successfully!")
        continue
    elif task_number == 2:
        print("Viewing tasks...")
        print("Tasks:")
        continue
    elif task_number == 3:
        print("Deleting task...")
        print("Task deleted successfully!")
        continue
    elif task_number == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid task number. Please try again.")