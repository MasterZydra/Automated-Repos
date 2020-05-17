import configparser

from . import constants
from .aureConfig import AureConfig

CONFIG_REPOS = "repos"
CONFIG_SECTION_JOB = "job "

class ConfigReader(object):
    @staticmethod
    def readConfig(file: str):
        aureConfig = AureConfig()

        config = configparser.ConfigParser()
        config.read(file)

        # Iterate through all sections
        for job in config.sections():
            if not job.lower().startswith(CONFIG_SECTION_JOB):
                continue
            # Add job to config
            aureConfig.addJob(job)

            # Iterate through all keys in section
            for key in config[job]:
                # Save repos to config
                if key.lower() == CONFIG_REPOS:
                    repos = config[job][key].split(constants.CONFIG_SEPARATOR)
                    for repo in repos:
                        aureConfig.addToJob(job, repo.strip())

        return aureConfig