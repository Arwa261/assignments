print("=== Welcome to To-Do List Program ===")
to_do_list = ["aya","esraa","zainab"]

while True:
  command = input("\nWrite a command (add, remove, view, exit): ").strip().lower()
  if command == "add":
   task = input("add your task:").strip()
   if task:  
            to_do_list.append(task)
            print(f" Task '{task}' added successfully!")
   else:
            print(" Task cannot be empty.")



  elif command == "remove":
    task = input("remove your task:").strip()
    if len(to_do_list) == 0:
            print("No tasks to remove.")
    elif task in to_do_list:
          to_do_list.remove(task)
          print(f"Task '{task}' removed successfully!")
          print (f"your to_do_list: {to_do_list}")

    else:
          print(f"Task '{task}' not found.")


  elif command == "view":
    if len(to_do_list) == 0:
     print ("no tasks to view")
    else:
     print (f"your to_do_list: {to_do_list}")


  elif command == "exit":
   print ("exit the program")
   break
  else:
   print("invalid command")