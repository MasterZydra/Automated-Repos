import os

# Import helper classes
from . import constants
from .aureConfig import AureConfig
from .configReader import ConfigReader

class ConfigWrapper(object):
    @staticmethod
    def configExists() -> bool:
        return os.path.exists(constants.AURE_CONFIG)
    
    @staticmethod
    def loadConfig() -> AureConfig:
        if ConfigWrapper.configExists():
            return ConfigReader.readConfig(constants.AURE_CONFIG)
        else:
            return None
    
    @staticmethod
    def writeConfig(config: AureConfig):
        ConfigReader.writeConfig(config)
