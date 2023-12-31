FILEPATH = 'todos.txt'


def get(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def save(todos, filepath=FILEPATH):
    """saves todo list to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)


def edit(list):
    """Runs editing mode for the list"""
    print("These are your to-dos:",)
    if not list:
        print("You have no To-dos")
    else:
        print("To-do List: ")
        # 'for' loop solution to remove '\n':
        # show_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     show_todos.append(new_item)
        for index, item in enumerate(list):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")
    reply = input("What would you like to do, clear, remove or replace? \n")
    if reply.startswith("clear"):
        list.clear()
        print("Your to-do list has been cleared.")
        save(list)
    elif reply.startswith("remove"):
        if len(reply) > 7:
            item = int(reply[6:])
        else:
            item = int(
                input("Which item would you like to remove?\n Specify a number: "))
        item = item - 1
        removed = list[item].strip('\n').capitalize()
        print(f"'{removed}', has been removed.")
        list.pop(item)
        save(list)
    elif reply.startswith("replace"):
        if len(reply) > 8:
            item = int(reply[7:])
        else:
            item = int(
                input("Which item would you like to replace?\n Specify a number: "))
        item = item - 1
        old = list[item].strip('\n')
        list[item] = input("Enter a new to-do: ") + "\n"
        new = list[item].strip('\n')
        print(f"'{old.capitalize()}' has been replaced by '{new}'")
        save(list)
    else:
        print("Invalid command.")


'''
to create an .exe in Windows:
pip install pyinstaller
->
pyinstaller --onefile --windowed --clean App1/gui.py

to create for Mac:
need 'hombrew' installed on mac. 
$ brew install --cask platypus
->
open platypus app and fill in. use absolute paths. for sctript type copy the absolute path of the interpretor (aka. python3). add main gui path to script path, and functions and other necesary script paths to bundled files.
'''
