# Handles the tasks, and commands
from task import *

tasks = []


def createTask(name, description):
    newTask = task(name, description)
    if len(tasks) <= 0:
        tasks.append(newTask)
    else:
        for i in range(len(tasks)):
            if tasks[i].getTaskStatus() == True:
                tasks.insert(i, newTask)
            elif i == (len(tasks) - 1):
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
    print("")


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
        print("Task " + taskID +" already completed")
    else:
        completeTask = tasks[int(taskID) - 1]
        tasks.remove(completeTask)
        tasks.append(completeTask)    
        completeTask.setComplete()
        print("Task " + taskID + " marked as complete")


def getAmountOfTasks():
    return len(tasks)
