class AureConfig(object):
    def __init__(self):
        self.__jobs = dict()

    def addJob(self, jobName: str):
        if jobName in self.__jobs:
            return
        
        self.__jobs[jobName] = list()
        return

    def addToJob(self, jobName: str, directory: str):
        self.addJob(jobName)
        self.__jobs.get(jobName).append(directory)

    def addListToJob(self, jobName: str, directories: list):
        self.addJob(jobName)
        self.__jobs.get(jobName).extend(directories)

    def getJob(self, jobName: str):
        if jobName in self.__jobs:
            return self.__jobs.get(jobName)
        return None
    
    def getJobs(self):
        return [*self.__jobs.keys()]