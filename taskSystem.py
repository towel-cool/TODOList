# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description):
    newTask = task(name, description)
    tasks.append(newTask)


def printAllTasks():
    print("List of all tasks\n---------------------------------------")
    for i in range(len(tasks)):
        print(str(i + 1) + '. ' + str(tasks[i]))
        print("---------------------------------------")


def removeTask(taskID):
    tasks.pop(int(taskID) - 1)
    print("Task " + taskID + " removed successfully")


def setTaskComplete(taskID):
    completeTask = tasks[int(taskID) - 1]
    completeTask.setComplete()


def getAmountOfTasks():
    return len(tasks)
# Creating Exceptions
