FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
        :purpose: Read a text file
        :return: list of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
        :purpose: Write the to-do list to the text file
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")