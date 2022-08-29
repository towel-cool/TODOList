from taskSystem import *

# Diego Diaz
# The purpose of this program is to keep track of tasks that you need to do

# TODO: UPDATING TASK STATUS, CREATE A COMPLETED TASKS COMMAND, FILE IO FOR TASKS, CHANGE HOW ID IS MADE


def main():
    command = ""
    while command != "QUIT":
        command = input("Command: ")
        command = command.upper()

        if command == "CREATE":
            name = input("Enter a task name: ")
            description = input("Enter a description: ")
            try:
                createTask(name, description)
            except:
                print("Error creating task")

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
            try:
                removeTask(taskID)
            except:
                print("Task " + taskID + " not found")

        elif command == "QUIT":
            print("Quitting...")

        else:
            print("Unknown Command " + command)


if __name__ == "__main__":
    main()
