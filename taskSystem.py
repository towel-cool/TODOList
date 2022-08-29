# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description):
    newTask = task(name, description)
    tasks.append(newTask)


def printTasks():
    for i in range(len(tasks)):
        print(str(i + 1) + '. ' + str(tasks[i]))


def removeTask(taskID):
    tasks.pop(int(taskID) - 1)
    print("Task " + taskID + " removed successfully")

def getAmountOfTasks():
    return len(tasks)
# Creating Exceptions
