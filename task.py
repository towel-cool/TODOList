class task:
    # Task class.
    # Creates a tasks with a name, description, and status of completion
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

    def setComplete(self):
        self.taskStatus = True

    def __repr__(self):
        if self.taskDescription != "":
            return self.taskName + "\nDescription: " + self.taskDescription + \
                "\nCompleted: " + str(self.taskStatus)
        return self.taskName + "\nCompleted: " + str(self.taskStatus)

    def __str__(self):
        if self.taskDescription != "":
            return self.taskName + "\nDescription: " + self.taskDescription + \
                "\nCompleted: " + str(self.taskStatus)
        return self.taskName + "\nCompleted: " + str(self.taskStatus)
