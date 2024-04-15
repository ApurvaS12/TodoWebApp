FILEPATH1 = "todos.txt"

def get_todos(filepath=FILEPATH1):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local



def write_todos(todos_arg, filepath=FILEPATH1):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def say_hello():
    print("your todo list")