class task:
    # Task class.
    # Creates a tasks with a name, descriptions and unique ID
    def __init__(self, taskName, taskDescription):
        self.taskName = taskName
        self.taskDescription = taskDescription
        self.taskStatus = False

    def getTaskName(self):
        return self.taskName

    def getTaskDescription(self):
        return self.taskDescription

    def getTaskStatus(self):
        return self.taskStatus

    def __repr__(self):
        return "Name: " + self.taskName + " Completed: " + str(self.taskStatus) + \
               " Description: " + self.taskDescription

    def __str__(self):
        return "Name: " + self.taskName + " Completed: " + str(self.taskStatus) + \
               " Description: " + self.taskDescription