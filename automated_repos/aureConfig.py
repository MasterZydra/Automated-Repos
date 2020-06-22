class AureConfig(object):
    def __init__(self):
        self.__jobs = dict()

    def addJob(self, jobName: str):
        if jobName in self.__jobs:
            return
        
        self.__jobs[jobName] = list()

    def remJob(self, jobName: str):
        if jobName in self.__jobs:
            return
        
        self.__jobs.pop(jobName)

    def addRepoToJob(self, jobName: str, directory: str):
        self.addJob(jobName)
        self.__jobs.get(jobName).append(directory)

    def addReposToJob(self, jobName: str, directories: list):
        self.addJob(jobName)
        self.__jobs.get(jobName).extend(directories)

    def getRepos(self, jobName: str):
        if jobName in self.__jobs:
            return self.__jobs.get(jobName)
        return None
    
    def getJobs(self):
        return [*self.__jobs.keys()]