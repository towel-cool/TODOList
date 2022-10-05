from taskSystem import *
import os

# Diego Diaz
# The purpose of this program is to act as a TODO List which will save tasks once exited and will reload them once opened


# File IO functions


def main():
    # Startup

    print("TODO List \nProgram created by Diego Diaz \nType 'help' to see a list of commands\nIMPORTANT: When exiting the program be sure to exit using the 'exit' command to ensure that all data is saved correctly")

    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    # Read the stored tasks file
    savedTasks = open(os.path.join(__location__, 'tasks.txt'),
                      "r", encoding="utf-8")
    readFile(savedTasks)
    savedTasks.close()

    # Open the file in read mode
    # The reason this is seperate from the statement above is because this statement overwrites the file
    # so I want to read the file before overwriting it
    savedTasks = open(os.path.join(__location__, 'tasks.txt'),
                      "a", encoding="utf-8")

    command = ""

    # Updated list of all commands and their purpose
    allCommands = {"TASKS": "List all tasks",
                   "CREATE": "Creates a new tasks",
                   "REMOVE": "Removes a task from the list of tasks",
                   "COMPLETE": "Marks a task as complete",
                   "SWAP": "Swaps the position of two tasks",
                   "CLEAR": "Clears the terminal",
                   "EXIT": "Exits the program"}

    while command != "EXIT":
        command = input("> ")
        command = command.upper()

        # Create tasks
        if command == "CREATE":
            name = input("Enter a task name: ")
            description = input("Enter a description (optional): ")
            try:
                createTask(name, description, False)
                writeFile(savedTasks)
            except:
                print("Error creating task")

        elif command == "SAVE":
            writeFile(savedTasks)

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
                writeFile(savedTasks)
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
                writeFile(savedTasks)
            except:
                print("Task " + taskID + " not found")

        elif command == "SWAP":
            if getAmountOfTasks() <= 0:
                print("No tasks to swap")
                continue
            taskID1 = input("Enter task number: ")
            taskID2 = input("Enter task number to swap with: ")
            try:
                swapTasks(taskID1, taskID2)
                writeFile(savedTasks)
            except:
                print("Error swapping tasks")

        elif command == "HELP":
            print("Note: Commands are not case sensitive\n")
            for i in allCommands:
                print(i + ': ' + allCommands.get(i))

        elif command == "CLEAR":
            clearCommand = "clear"
            if os.name in ('nt', 'dos'):
                command = "cls"
            os.system(clearCommand)

        # Quit the program
        elif command == "EXIT":
            writeFile(savedTasks)
            savedTasks.close()
            print("Exiting...")

        # Unknown command
        else:
            print("Unknown command " + command +
                  "\nType 'help' to see a list of commands")


if __name__ == "__main__":
    main()
