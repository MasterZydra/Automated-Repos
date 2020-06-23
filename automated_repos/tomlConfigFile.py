import toml

from . import constants
from .aureConfig import AureConfig

class TomlConfigFile(object):
    @staticmethod
    def readConfig(file: str) -> AureConfig:
        aureConfig = AureConfig()

        tomlObj = toml.load(file)

        # Jobs
        if 'jobs' in tomlObj:
            for job in tomlObj['jobs']:
                # Add job to AuRe config
                aureConfig.addJob(job)
                # Add repos to job
                if 'repos' in tomlObj['jobs'][job]:
                    aureConfig.addReposToJob(job, tomlObj['jobs'][job]['repos'])
        
        return aureConfig

    @staticmethod
    def writeConfig(config: AureConfig):
        # Create empty TOML object
        tomlObj = dict()
        # Add dict for jobs
        tomlObj['jobs'] = dict()

        jobs = config.getJobs()
        for job in jobs:
            # Create jobs
            tomlObj['jobs'][job] = dict()
            # Add repos
            tomlObj['jobs'][job]['repos'] = config.getRepos(job)

        # Convert TOML object to TOML string
        tomlStr = toml.dumps(tomlObj)

        # Save TOML string to file
        f = open(constants.AURE_CONFIG, 'w')
        f.write(tomlStr)