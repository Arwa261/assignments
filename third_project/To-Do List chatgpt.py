print("=== Welcome to To-Do List Program ===")

# قائمة فارغة لتخزين المهام
to_do_list = ["aya", "esraa", "zainab"]

# ----- Functions -----
def add_task():
    task = input("Add your task: ").strip()
    if task:
        to_do_list.append(task)
        print(f"✅ '{task}' added to the list.")
        print(f"\n📋 Your To-Do List: {to_do_list}")
    else:
        print("⚠️ You entered an empty task.")

def remove_task():
    task = input("Enter the task you want to remove: ").strip()
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"🗑️ '{task}' removed from the list.")
    else:
        print(f"⚠️ '{task}' not found in the list.")

def view_tasks():
    if not to_do_list:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")

def exit_program():
    print("👋 Goodbye! Thanks for using the To-Do List program.")
    exit()

# ----- Main Loop -----
while True:
    command = input("\nWrite a command (add, remove, view, exit): ").strip().lower()
    
    if command == "add":
        add_task()
    elif command == "remove":
        remove_task()
    elif command == "view":
        view_tasks()
    elif command == "exit":
        exit_program()
    else:
        print("⚠️ Invalid command, please try again.")
