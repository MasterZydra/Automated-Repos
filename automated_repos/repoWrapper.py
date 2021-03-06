# Import helper classes
from . import constants
from .aureConfig import AureConfig
from .configWrapper import ConfigWrapper

class RepoWrapper(object):
    @staticmethod
    def addRepo(job: str, repo: str):
        pass
        # Load config
        config = ConfigWrapper.loadConfig()
        # Init new config if it does not exist yet
        if config is None:
            config = AureConfig()

        config.addRepoToJob(job, repo.lower())

        # Save config
        ConfigWrapper.writeConfig(config)

    @staticmethod
    def remRepo(job: str, repo: str):
        pass
        # Load config
        config = ConfigWrapper.loadConfig()
        # Init new config if it does not exist yet
        if config is None:
            return

        config.remRepoFromJob(job, repo.lower())

        # Save config
        ConfigWrapper.writeConfig(config)

    @staticmethod
    def showRepo():
        pass
        # Load config
        #config = ConfigWrapper.loadConfig()
        # Init new config if it does not exist yet
        #if config is None:
        #    print(constants.ERROR + constants.MSG_NO_AURE_CONFIG)
        #    return

        #sep = ', '

        #config.getJobs().sort()
        #jobs = sep.join(config.getJobs())

        #print('Jobs:')
        #print('-----')
        #print(jobs)
        #print('')
        #print('Details:')
        #print('--------')
        #for job in config.getJobs():
        #    print('- ' + job + ':')

        #    print('')