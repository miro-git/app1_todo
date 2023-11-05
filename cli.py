import functions
import time

dashes = "-" * 50
print(
    f'{dashes}\n'
    f'--\t {time.strftime("%b %d, %Y")} \n'
    f'--\t {time.strftime("%H:%M")} \n'
    f'{dashes}\n'
)

while True:
    user_action = input("Type add, show, edit #, complete #, or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)
        print(dashes)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}-{todo}"
            print(row)
        print(dashes)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number -= 1
            todos = functions.get_todos()

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        finally:
            print(dashes)
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = functions.get_todos()
            if number > len(todos):
                print("There is no item with that number.")
                continue
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            print(f"The task '{todo_to_remove}' was completed. ")
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid. Please specify the number of the task to be completed.")
        finally:
            print(dashes)
    elif user_action.startswith("exit"):
        break
    else:
        print(f"Invalid command: {user_action}")
        print(dashes)

print("Bye!")
