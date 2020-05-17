import os

# Import helper classes
from . import help_exec
from . import constants
from .gitWrapper import GitWrapper
from .gitLanguages import GitLanguages
from .params import Params

class Exec(object):
    def __init__(self, params: Params):
        self.__params = params
        self.__gitMessages = None
    
    def run(self):
        if self.__params.arg0 in ('--help', 'help'):
            self.__printHelp()
            return
        
        elif len(self.__params.args) == 0: # or -- all ....
            if not self.__checkEnv():
                return
                return
            
            status = GitWrapper.getGitStatus(self.__gitMessages)
        else:
            self.__printHelp()
            return

    def __checkEnv(self):
        # Check if config file is in directory or parent directories
        if not os.path.exists(constants.AURE_CONFIG):
            print(constants.ERROR + constants.MSG_NO_AURE_CONFIG)
            return False
        
        # Check if git is installed
        if not GitWrapper.isGitInstalled():
            print(constants.ERROR + constants.MSG_NO_GIT_INSTALLED)
            return False
        
        # Identify git language
        if not self.__importGitMessages(GitWrapper.getGitLanguage()):
            return False
        
        return True

    def __importGitMessages(self, langauge: GitLanguages):
        if langauge == GitLanguages.UNKNOWN:
            print(constants.ERROR + constants.MSG_LANG_IS_UNKNOWN)
            return False
        if langauge == GitLanguages.DE:
            from .gitMessages_DE import GitMessages_DE
            self.__gitMessages = GitMessages_DE
        elif langauge == GitLanguages.EN:
            from .gitMessages_EN import GitMessages_EN
            self.__gitMessages = GitMessages_EN
        else:
            print(constants.ERROR + constants.MSG_LANG_NOT_SUPPORTED)
            return False
        
        return True


    def __printHelp(self):
        print(help_exec.__doc__)