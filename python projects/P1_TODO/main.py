import functions
import time
print(f"It is {time.strftime('%b %d,%Y %H:%M:%S')}")
functions.say_hello()
while True:
    user_action = input("type add, show, edit, complete or exit:").strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)
        
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number -1
            todos = functions.get_todos()
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number -1
            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            print(f"todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("there is no item with that number")
          


    elif user_action.startswith("exit"):
        break