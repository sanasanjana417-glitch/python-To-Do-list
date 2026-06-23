my_tasks = []

while True:
    task = input("Enter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    my_tasks.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(my_tasks, start=1):
    print(f"{i}. {task}")