from taskSystem import *

# TODO: EXCEPTIONS, DELETING TASKS, UPDATING TASKS STATUS, CREATE A COMPLETED TASKS COMMAND, FILE IO FOR TASKS, CHANGE HOW ID IS MADE


def main():
    command = ""
    while command != "QUIT":
        command = input("Command: ")
        command = command.upper()
        if command == "CREATE":
            name = input("Enter a task name: ")
            description = input("Enter a description: ")
            createTask(name, description)
        elif command == "TASKS":
            printTasks()
        else:
            print("Unknown Command " + command)


if __name__ == "__main__":
    main()
