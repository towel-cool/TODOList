from taskSystem import *

# Diego Diaz
# The purpose of this program is to keep track of tasks that you need to do

# TODO: DELETING TASKS, UPDATING TASKS STATUS, CREATE A COMPLETED TASKS COMMAND, FILE IO FOR TASKS, CHANGE HOW ID IS MADE
# MAYBE: EXCEPTIONS


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
            if getAmountOfTasks() <= 0:
                print("No tasks")
                continue
            printTasks()

        elif command == "REMOVE":
            if getAmountOfTasks() <= 0:
                print("No tasks to remove")
                continue
            taskID = input("Enter Task Number: ")
            removeTask(taskID)

        elif command == "QUIT":
            print("Quitting...")

        else:
            print("Unknown Command " + command)


if __name__ == "__main__":
    main()
