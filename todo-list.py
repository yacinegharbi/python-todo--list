while True:
    print("simple python todo-list")
    print("the menu:")
    print("1/ add a task")
    print("2/ modifie a task")
    print("3/ remove a task")
    print("4/show all tasks")
    print("5/ exit")

    choose = input("please choose an option: ")
    if choose == "1":
        with open(r"C:\Users\TRETEC\todo-list.txt", "a") as f:
            user_input = input("add your new task: ")
            f.write(user_input + "\n")
        print("Task added!")

    elif choose == "2":
        with open(r"C:\Users\TRETEC\todo-list.txt", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line_number = int(input("Which line to modify? ")) - 1
                print(f"{i}, {line.strip()}")
                user_input = input("enter the modified line: ")
                lines[line_number] = user_input + "\n"
                with open(r"C:\Users\TRETEC\todo-list.txt", "w") as f:
                    f.writelines(lines)
                print("task modified")
    elif choose == "3":
        with open(r"C:\Users\TRETEC\todo-list.txt", "r") as f:
            lines = f.readlines()
        if len(lines) == 0:
            print("No tasks to remove.")
        else:
            for i, line in enumerate(lines):
                print(f"{i+1}/ {line.strip()}")
            try:
                line_number = int(input("Which line to remove? ")) - 1
                if line_number < 0 or line_number >= len(lines):
                    raise IndexError
                removed_line = lines.pop(line_number)
                with open(r"C:\Users\TRETEC\todo-list.txt", "w") as f:
                    f.writelines(lines)
                print(f"Removed task: {removed_line.strip()}")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print(
                    "Error: line number out of range. Please choose a valid task number.")
    elif choose == "4":
        with open(r"C:\Users\TRETEC\todo-list.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No tasks yet!")
            else:
                for i, line in enumerate(lines):
                    print(f"{i+1}/ {line.strip()}")
    elif choose == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
