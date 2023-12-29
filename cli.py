from functions import *
import time

now = time.strftime(("%b %d, %Y %H:%M:%S"))
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        # w - means write, r - read a file
        write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        new_todos = []
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"🔥 {index + 1} - {item};")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter a new to do:  ")

            todos[number] = new_todo + '\n'

            write_todos(todos_arg=todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            # function to delete an item from the list
            todos.pop(number - 1)

            write_todos(todos_arg=todos)
            message = f"Task:  {todo_to_remove} was removed from the list 👌"
            print(message)

        except IndexError:
            print("Your command is not valid, enter a valid number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid 🤬")
print("Bye")


person_name = input("Enter your name: ")


