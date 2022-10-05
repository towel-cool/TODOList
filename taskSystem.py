# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description, status):
    newTask = task(name, description, status)
    if len(tasks) <= 0:
        tasks.append(newTask)
    else:
        for i in range(len(tasks)):
            if tasks[i].getTaskStatus() == True:
                tasks.insert(i, newTask)
                break
            elif i == (len(tasks) - 1):
                tasks.append(newTask)
                break


def printAllTasks():
    incompleteTasks = []
    completeTasks = []

    for i in tasks:
        if i.getTaskStatus() == False:
            incompleteTasks.append(i)
        else:
            completeTasks.append(i)

    print("\n---------------------------------------\nIncomplete Tasks\n---------------------------------------")
    for i in range(len(incompleteTasks)):
        print(str((i + 1)) + '. ' + incompleteTasks[i].getTaskName())
        if (len(incompleteTasks[i].getTaskDescription()) > 0):
            print("Description: " + incompleteTasks[i].getTaskDescription())
        print("Completed: " + str(incompleteTasks[i].getTaskStatus()))

    print("\n---------------------------------------\nComplete Tasks\n---------------------------------------")
    for i in range(len(completeTasks)):
        print(str((i + len(incompleteTasks) + 1)) +
              '. ' + completeTasks[i].getTaskName())
        if (len(completeTasks[i].getTaskDescription()) > 0):
            print("Description: " + completeTasks[i].getTaskDescription())
        print("Completed: " + str(completeTasks[i].getTaskStatus()))

def removeTask(taskID):
    tasks.pop(int(taskID) - 1)
    print("Task " + taskID + " removed successfully")


def swapTasks(taskID1, taskID2):
    if (tasks[int(taskID1) - 1].getTaskStatus() == False and tasks[int(taskID2) - 1].getTaskStatus() == False) \
            or (tasks[int(taskID1) - 1].getTaskStatus() == True and tasks[int(taskID2) - 1].getTaskStatus() == True):
        task1 = tasks[int(taskID1) - 1]
        task2 = tasks[int(taskID2) - 1]
        tasks.remove(task1)
        tasks.insert(int(taskID1) - 1, task2)
        tasks.remove(task2)
        tasks.insert(int(taskID2) - 1, task1)
        print("Task " + taskID1 + " swapped with task " + taskID2)
    else:
        print("Cannot swap completed tasks with incomplete tasks")


def setTaskComplete(taskID):
    if tasks[int(taskID) - 1].getTaskStatus() == True:
        print("Task " + taskID + " already completed")
    else:
        completeTask = tasks[int(taskID) - 1]
        tasks.remove(completeTask)
        tasks.append(completeTask)
        completeTask.setComplete()
        print("Task " + taskID + " marked as complete")


def readFile(f):
    # Read from the existing file of tasks and create each task and store it in the tasks list
    savedTasks = f.readlines()
    for task in savedTasks:
        task = task.split('-')
        if (len(task) == 3):
            status = task[0]
            name = task[1]
            description = task[2]
            # Stripping the \n from the description
            description = description[0:len(description)-1]
            if (status == "True"):
                status = True
            elif (status == "False"):
                status = False
            createTask(name, description, status)


def writeFile(f):
    # Delete the contents of a file and rewrite it with the new list of tasks
    f.truncate(0)
    allTasksString = ""
    for t in tasks:
        taskString = str(t.getTaskStatus()) + '-' + str(t.getTaskName()
                                                        ) + '-' + str(t.getTaskDescription()) + "\n"
        allTasksString = allTasksString + taskString
    f.write(allTasksString)


def getAmountOfTasks():
    return len(tasks)
