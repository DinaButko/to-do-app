import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do", background_color="pink", font="bold")

# Boxes
input_box = sg.InputText(tooltip="Enter to-do", text_color="black", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])

# Buttons
add_button = sg.Button("Add", button_color="violet", font="bold")
edit_button = sg.Button("Edit", button_color="violet", font="bold")

# Window
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   background_color="pink", font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')

            # w - means write, r - read a file
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break








window.close()
