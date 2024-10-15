print("-------ToDo App-------")
print("1. Add Task")
print("2. Remove Task")
print("3. View Task")
print("4. Exit App")

def ToDo():
  tasks=[]
  choice=input("Enter what you want to do: ")
  choice=choice.upper()

  while True:
    if choice == "ADD" or choice == "ADD TASK":
      task = input("Enter task you want add: ")
      if task in tasks:
        print(f"{task} is in {tasks}")
      else:
        tasks.append(task)
        print(f"{task} added!{tasks}")
    elif choice == "REMOVE" or choice == "REMOVE TASK":
      remo = input("Which task you want to remove? ")
      if remo in tasks:
        tasks.remove(remo)
        print(f"{task} removed! {tasks}")
      else:
        print(f"{remo} not found! {tasks}")
    elif choice == "VIEW" or choice == "VIEW TASK":
      print(tasks)
    else:
      break

    choice=input("Enter what you want to do: ")
    choice=choice.upper()

ToDo()