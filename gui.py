import functions
import PySimpleGUI as sg

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
    if event == "ListboxClick":
        print("selected: ", values['ListboxClick'][0])
        window['new_todo'].update(value=values['ListboxClick'][0])

    if event.lower() == "add":
        todos = functions.get_todos()
        new_todo = values['new_todo'] + "\n"
        print(2, "adding: ", str(values['new_todo']).replace("\n", ""))
        todos.append(new_todo)
        functions.write_todos(todos)
        window['new_todo'].update(value='')
        window['ListboxClick'].update(values=todos)

    if event.lower() == "edit":
        print(2, "replace: ", values['ListboxClick'])
        todo_to_change = values['ListboxClick'][0]
        print(3, "with: ", str(values['new_todo']).replace("\n", ""))
        new_todo = values['new_todo'] + "\n"
        todos = functions.get_todos()
        todo_to_change_index = todos.index(todo_to_change)
        todos[todo_to_change_index] = new_todo
        functions.write_todos(todos)
        window['ListboxClick'].update(values=todos)

    if event.lower() == "complete":
        print(2, "complete: ", values['ListboxClick'])
        todo_to_complete = values['ListboxClick'][0]
        todos = functions.get_todos()
        # todo_to_complete_index = todos.index(todo_to_complete)
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['ListboxClick'].update(values=todos)
        window['new_todo'].update(value='')

    if event.lower() == "exit":
        break

    if event == sg.WIN_CLOSED:
        break

window.close()
