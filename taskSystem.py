# Handles the tasks, and commands
from task import *

tasks = {}


def createTask(name, description):
    newTaskID = len(tasks) + 1
    newTask = task(name, description, newTaskID)
    tasks.update({str(newTaskID): newTask})


def printTasks():
    for i in tasks:
        print(i)
    print(tasks)


def removeTask(taskID):
    try:
        tasks.pop(str(taskID))
    except :
        print("Task " + taskID + " does not exist")


def getAmountOfTasks():
    return len(tasks)
# Creating Exceptions
