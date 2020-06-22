import os

# Import helper classes
from . import constants
from .aureConfig import AureConfig
from .tomlConfigFile import TomlConfigFile

class ConfigWrapper(object):
    @staticmethod
    def configExists() -> bool:
        return os.path.exists(constants.AURE_CONFIG)
    
    @staticmethod
    def loadConfig() -> AureConfig:
        if ConfigWrapper.configExists():
            return TomlConfigFile.readConfig(constants.AURE_CONFIG)
        else:
            return None
    
    @staticmethod
    def writeConfig(config: AureConfig):
        TomlConfigFile.writeConfig(config)
