class AureConfig(object):
    def __init__(self):
        self.__jobs = dict()

    def addJob(self, jobName: str):
        if jobName in self.__jobs:
            return
        
        self.__jobs[jobName] = list()

    def remJob(self, jobName: str):
        if not jobName in self.__jobs:
            return
        
        self.__jobs.pop(jobName)

    def addRepoToJob(self, jobName: str, directory: str):
        self.addJob(jobName)
        if not directory in self.__jobs[jobName]:
            self.__jobs.get(jobName).append(directory)

    def remRepoFromJob(self, jobName: str, directory: str):
        if not jobName in self.__jobs:
            return
        
        if directory in self.__jobs[jobName]:
            self.__jobs[jobName].remove(directory)

    def addReposToJob(self, jobName: str, directories: list):
        self.addJob(jobName)
        self.__jobs.get(jobName).extend(directories)

    def getRepos(self, jobName: str) -> list:
        if jobName in self.__jobs:
            return self.__jobs.get(jobName)
        return None
    
    def getJobs(self) -> list:
        return [*self.__jobs]