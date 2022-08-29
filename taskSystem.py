# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description):
    newTaskID = len(tasks) + 1
    newTask = task(name, description, newTaskID)
    tasks.append(newTask)


def printTasks():
    for i in tasks:
        print(i)


# Creating Exceptions
