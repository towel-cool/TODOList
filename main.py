from taskSystem import *

# Diego Diaz
# The purpose of this program is to keep track of tasks that you need to do

# TODO: UPDATING TASK STATUS, CREATE A COMPLETED TASKS COMMAND, FILE IO FOR TASKS, CHANGE HOW ID IS MADE


def main():
    command = ""
    while command != "QUIT":
        command = input("Command: ")
        command = command.upper()

        # Create tasks
        if command == "CREATE":
            name = input("Enter a task name: ")
            description = input("Enter a description: ")
            try:
                createTask(name, description)
            except:
                print("Error creating task")

        # Print all tasks
        elif command == "TASKS":
            if getAmountOfTasks() <= 0:
                print("No tasks")
                continue
            printAllTasks()

        # Remove a given task
        elif command == "REMOVE":
            if getAmountOfTasks() <= 0:
                print("No tasks to remove")
                continue
            taskID = input("Enter task number: ")
            try:
                removeTask(taskID)
            except:
                print("Task " + taskID + " not found")

        # Set a task to complete
        elif command == "COMPLETE":
            if getAmountOfTasks() <= 0:
                print("No tasks to complete")
                continue
            taskID = input("Enter task number: ")
            try:
                setTaskComplete(taskID)
            except:
                print("Task " + taskID + " not found")

        # Quit the program
        elif command == "QUIT":
            print("Quitting...")

        # Unknown command
        else:
            print("Unknown command " + command)


if __name__ == "__main__":
    main()
