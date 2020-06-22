import toml

from . import constants
from .aureConfig import AureConfig

class ConfigReader(object):
    @staticmethod
    def readConfig(file: str) -> AureConfig:
        aureConfig = AureConfig()

        tomlObj = toml.load(file)

        # Jobs
        if 'jobs' in tomlObj:
            for job in tomlObj['jobs']:
                aureConfig.addJob(job)
        
        return aureConfig

    @staticmethod
    def writeConfig(config: AureConfig):
        # Build TOML object
        tomlObj = dict()

        tomlObj['jobs'] = dict()

        for job in config.getJobs():
            tomlObj['jobs'][job] = dict()
        
        tomlStr = toml.dumps(tomlObj)
        f = open(constants.AURE_CONFIG, 'w')
        f.write(tomlStr)