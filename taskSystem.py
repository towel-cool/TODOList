# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description):
    newTask = task(name, description)
    tasks.append(newTask)


def printAllTasks():
    print("\n---------------------------------------\nIncomplete Tasks\n---------------------------------------")
    indexOfFirstCompleteTask = -1
    tasksAreComplete = False
    for i in range(len(tasks)):
        if tasks[i].getTaskStatus() == True:
            tasksAreComplete = True
            indexOfFirstCompleteTask = i
            break
        print(str(i + 1) + '. ' + str(tasks[i]))

    print("\n---------------------------------------\nComplete Tasks\n---------------------------------------")
    if tasksAreComplete:
        for i in range(indexOfFirstCompleteTask, len(tasks)):
            print(str(i + 1) + '. ' + str(tasks[i]))


def removeTask(taskID):
    tasks.pop(int(taskID) - 1)
    print("Task " + taskID + " removed successfully")


def setTaskComplete(taskID):
    completeTask = tasks[int(taskID) - 1]
    tasks.remove(completeTask)
    tasks.append(completeTask)    
    completeTask.setComplete()


def getAmountOfTasks():
    return len(tasks)
