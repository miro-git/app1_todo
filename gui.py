import functions
import PySimpleGUI as sg
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

#  create all windows elements
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter to-do", key="new_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='ListboxClick',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 16))
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    event, values = window.read()
    print(1, "event: ", event)

    if event == sg.WIN_CLOSED:
        break

    if event == "ListboxClick":
        print("selected: ", values['ListboxClick'][0])
        window['new_todo'].update(value=values['ListboxClick'][0].strip())

    if event.lower() == "add":
        new_todo_stripped = values['new_todo'].strip()
        print(2, "add: ", new_todo_stripped)
        if not new_todo_stripped:
            sg.popup("No item entered yet!")
        else:
            new_todo = new_todo_stripped + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['new_todo'].update(value='')
            window['ListboxClick'].update(values=todos)

    if event.lower() == "edit":
        print(2, "replace: ", str(values['ListboxClick'][0]).replace("\n", ""))
        try:
            todo_to_change = values['ListboxClick'][0]
            print(3, "with: ", str(values['new_todo']).replace("\n", ""))
            new_todo = values['new_todo'] + "\n"
            todos = functions.get_todos()
            todo_to_change_index = todos.index(todo_to_change)
            todos[todo_to_change_index] = new_todo
            functions.write_todos(todos)
            window['new_todo'].update(value='')
            window['ListboxClick'].update(values=todos)
        except IndexError:
            sg.popup("No item selected!")

    if event.lower() == "complete":
        print(2, "complete: ", values['ListboxClick'][0].strip())
        try:
            todo_to_complete = values['ListboxClick'][0]
            todos = functions.get_todos()
            # todo_to_complete_index = todos.index(todo_to_complete)
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['ListboxClick'].update(values=todos)
            window['new_todo'].update(value='')
        except IndexError:
            sg.popup("No item selected!")

    if event.lower() == "exit":
        break


window.close()
