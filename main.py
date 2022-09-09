from taskSystem import *

# Diego Diaz
# The purpose of this program is to act as a TODO List

# TODO: FILE IO FOR TASKS 
# FIX THE BUG WHERE TASKS ARE PRINTING UNDER THE COMPLETED TASKS TAB WHEN THEY ARE CREATED AFTER A TASK IS COMPLETE


def main():
    print("TODO List \nProgram created by Diego Diaz \nType 'help' to see a list of commands")
    command = ""
    #Updated list of all commands and their purpose
    allCommands = {"TASKS" : "List all tasks",
                    "CREATE" : "Creates a new tasks",
                    "REMOVE" : "Removes a task from the list of tasks",
                    "COMPLETE" : "Marks a task as complete",
                    "CLEAR" : "Clears the terminal",
                    "QUIT" : "Exits the program"}

    while command != "QUIT":
        command = input("> ")
        command = command.upper()

        # Create tasks
        if command == "CREATE":
            name = input("Enter a task name: ")
            description = input("Enter a description (optional): ")
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

        elif command == "HELP":
            print("Note: Commands are not case sensitive\n")
            for i in allCommands:
                print(i + ': ' + allCommands.get(i))
        
        elif command == "CLEAR":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Quit the program
        elif command == "QUIT":
            print("Quitting...")

        # Unknown command
        else:
            print("Unknown command " + command + "\nType 'help' to see a list of commands")


if __name__ == "__main__":
    main()
    