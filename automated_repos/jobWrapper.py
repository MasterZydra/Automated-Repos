# Import helper classes
from .aureConfig import AureConfig
from .configWrapper import ConfigWrapper

class JobWrapper(object):
    @staticmethod
    def addJob(job: str):
            # Load config
            config = ConfigWrapper.loadConfig()
            # Init new config if it does not exist yet
            if config is None:
                config = AureConfig()

            config.addJob(job)

            # Save config
            ConfigWrapper.writeConfig(config)